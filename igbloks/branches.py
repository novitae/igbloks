from typing import Any, Self, Callable, Optional, SupportsIndex
from .utils import *

__all__ = ( "MultipleKeyField", "BlokField", "Branch", "MultipleBranches",
            )

class MultipleKeyField:
    """
        `MultipleKeyField` is the base of `BlokField`, `Branch` and
        `MultipleBranches`. It contains the aliases of each item. You
        shouldn't use it if you don't know what you're doing.
    """
    def __init__(
        self,
        aliases: dict[str, str]
    ) -> None:
        self.aliases = aliases

    @property
    def aliases(self) -> dict[str, str]:
        return self._aliases
    
    @aliases.setter
    def aliases(self, aliases: dict[str, str]) -> None:
        assert isinstance(aliases, dict)
        assert all([ isinstance(key, str) and isinstance(value, str)
                     for key, value in aliases.items() ])
        self._aliases = aliases

    def __to_py_obj__(
        self,
        content: dict[str, dict[str, Any]],
        bkid: str,
        *,
        verified: bool = False,
    ) -> Self:
        ...

    def __to_bloks__(self, *args, **kwargs) -> dict:
        ...


class BlokField(MultipleKeyField):
    def __init__(
        self,
        aliases: dict[str, str],
        required: bool = False,
        default: Any = Undefined,
        default_factory: Callable[[Optional[Any], Any], Any] = None,
        import_transformer: Callable[[Any, Optional[str]], Any] = None,
        export_transformer: Callable[[Any], Any] = None,
        accepted_types: set[type | Self] = None,
        skip_type_verif: bool = False,
    ) -> None:
        """
            Field for IG Blok branches.
            - `aliases` (`dict[str, str]`): Must be a dict mapping name of the field to
                its bkid. As an example:

            ```json
                {
                    "5d9af7318e9ff0ac69aa387c21c0913044bd3067683554a96c0024aa52262e82": "bk.components.Flexbox",
                    "4c3949f30190b147b88e668dc21792a7f419412a90a8d59ccc44ec3c46a2cb08": "㐈",
                }
            ```
            - `required` (`bool`): `True` to make the field required, otherwise `False`.
            - `default` (`Any`): The default value to be placed if the field is required
                but no value have been passed in. Also check the next arg.
            - `default_factory`: It must be a callable, that takes no arguments, and it
                will be used to use its return value for the value of the field.
            - `import_transformer` (`FunctionType`): It must be a callable (function 
                or lambda) that must take at least one argument. When the raw value for 
                the field will be found, it will call this callable, with the argument
                `value` (`Any`). Its result will be the value placed as the value of the
                field in the branch. Make sure the result will have the `accepted_types`
                you filled in, or deactivate `skip_type_verif`. By default it will
                return the value untouched.
            - `export_transformer` (`FunctionType`): In the same style as the argument
                `import_transformer`, it will be executed on the value of the field and
                then used in the export result. It can take only one argument `value` (
                `Any`). It will return by default the untouched value of the field.
            - `accepted_types` (`[set | list | tuple ][type | Branch]`): The list of the
                types accepted for the field. The type that will be verified is the one
                returned by the `import_transformer` function. If you put an instance of
                `Branch` in the types, the item passed in the field will look for matches
                with its branch name (if it is a branch) and the aliases of each possible
                branches in the types. If it doesn't find anything, it will then return
                the value of `import_transformer`. By default, the value of this variable
                will be set to the type(s) placed as annotations.
            - `skip_type_verif` (`bool`): If placed on `True` it will ignore verification
                of the return type of `import_transformer`. It is by default on `True`.
        """
        super().__init__(aliases=aliases)

        if default == Undefined and default_factory is None:
            if required is True:
                raise # Pas de valeur par défaut ou qui sera générée
        elif default_factory is not None and default != Undefined:
            raise # On ne sait pas le quel choisir
        elif default_factory is not None:
            if callable(default_factory) is False:
                raise # Pas callable
        else:
            def _default_fact_from_default(value: Any, *args, **kwargs) -> Any:
                return value
            default_factory = _default_fact_from_default

        self.required = required
        self.default_factory = default_factory
        self.accepted_types = accepted_types
        self.skip_type_verif = skip_type_verif

        def _mprt_trsf(value: Any) -> Any:
            return value
        self.import_transformer = _mprt_trsf if import_transformer is None else import_transformer
        def _xprt_trsf(value: Any) -> Any:
            return value
        self.export_transformer = _xprt_trsf if export_transformer is None else export_transformer

    def __repr__(self) -> str:
        return ( f"BlokField(required: {self.required}, "
                 f"accepted_types: {tuple(map(lambda item: item.__name__, self.accepted_types))}, "
                 f"aliases: {tuple(self.aliases.values())}, "
                 f"pretty_name: \"{self.pretty_name}\")" )
    
    @check_return_type
    def __to_py_obj__(self, content: Any, bkid: str, *, verified: bool = False) -> Self:
        value = self._import_transformer(content)
        if (name := branch_name(content)) is not None:
            sub_branches = { item.aliases[bkid]: item for item in self.accepted_types
                             if item is self.__class__ }
            if (matching_btype := sub_branches.get(name)) is not None:
                return matching_btype.__to_py_obj__( content=value,
                                                     bkid=bkid,
                                                     verified=True )
        return value
    
    @property
    def import_transformer(self) -> Callable[[Any], Any]:
        return self._import_transformer
    
    @import_transformer.setter
    def import_transformer(self, transformer: Callable[[Any], Any]) -> None:
        assert callable(transformer)
        self._import_transformer = transformer

    @property
    def export_transformer(self) -> Callable[[Any], Any]:
        return self._export_transformer
    
    @export_transformer.setter
    def export_transformer(self, transformer: Callable[[Any], Any]) -> None:
        assert callable(transformer)
        self._export_transformer = transformer

    @property
    def pretty_name(self) -> str | None:
        """The readable name of the field"""
        return self._pretty_name
    
    @pretty_name.setter
    def pretty_name(self, name: str) -> None:
        assert isinstance(name, str)
        self._pretty_name = name

    @property
    def accepted_types(self) -> set[type | Self] | None:
        return self._accepted_types
    
    @accepted_types.setter
    def accepted_types(self, accepted_types: set[type | Self] | None) -> None:
        if accepted_types is not None:
            if isinstance(accepted_types, set) is False:
                if isinstance(accepted_types, (tuple, list)):
                    accepted_types = set(accepted_types)
                else:
                    raise # Pas un set
            if not all([isinstance(item, type) for item in accepted_types]):
                raise # Ne contient pas que des type
        self._accepted_types = accepted_types

class Branch(MultipleKeyField):
    """
        Make sure to add a type to every fields, otherwise it won't
        be readen.
        - `aliases`: A dict of `bkid: name`
    """
    aliases: dict[str, str]

    def __init__(self) -> None:
        raw_fields = self.__class__.__annotations__.copy()
        if "aliases" in raw_fields:
            del raw_fields["aliases"]
        super().__init__(aliases=self.__class__.__dict__["aliases"])
        
        self.fields: dict[str, BlokField] = {}
        for field_name, field_types in raw_fields.items():
            field_types = annotation_types(field_types)
            field_value = self.__class__.__dict__.get(field_name, Undefined)
            if isinstance(field_value, BlokField):
                if field_value.accepted_types is None:
                    field_value.accepted_types = field_types
                if field_value.pretty_name is None:
                    field_value.pretty_name = field_name
                self.fields[field_name] = field_value
            else:
                raise TypeError # Il faut que ce soit un type
            
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in self.fields:
            field = self.fields[__name]
            __value = field(key=__name, value=__value)
            if field.skip_type_verif is False:
                assert isinstance(__value, field.accepted_types)
        return super().__setattr__(__name, __value)
            
    def __to_py_obj__(
        self,
        content: dict[str, dict[str, Any]],
        bkid: str,
        *,
        verified: bool = False,
    ) -> Self:
        if verified is False:
            assert is_branch(content)
        key_to_field = { field.aliases[bkid]: field for field in self.fields.values() }
        for values in content.values():
            for key, value in values.items():
                if key in key_to_field:
                    field = key_to_field[key]
                    setattr(
                        self,
                        field.pretty_name,
                        field.__to_py_obj__(value, key)
                    )
                else:
                    raise KeyError( f'unknown key "{key}" in fields of "'
                                    f'{self.__class__.__name__}" for bkid'
                                    f' "{bkid}".' )
        return self

    def to_bloks(self) -> dict:
        ""

class MultipleBranches(MultipleKeyField):
    aliases: dict[str, str]
    discriminator: list[Branch]

    def __init__(self) -> None:
        try:
            super().__init__(aliases=self.__class__.__dict__["aliases"])
            discriminator = self.__class__.__dict__["discriminator"]
        except KeyError as error:
            raise AttributeError( 'field "aliases" or "discriminator" has no '
                                  'value attributed to itself. Make sure you '
                                  'did not forget to set them before initating'
                                  ' the child of this class.' ) from error
        assert isinstance(discriminator, (tuple, set, list))
        assert all([isinstance(item, Branch) for item in discriminator])
        self._discriminator: list[Branch] = discriminator
        self._values = []

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self._values)})"
    
    def __to_py_obj__(
        self,
        content: list[dict],
        bkid: str,
        **kwargs
    ) -> list[Branch]:
        assert isinstance(content, list)
        branch_names = [ branch_name(item) for item in content ]
        assert all([ item is not None for item in branch_names ])

        key_to_branch = { field.aliases[bkid]: field for field in self._discriminator }
        result = []
        for alias, raw_branch in zip(content, branch_names):
            try:
                result.append(key_to_branch[alias].__to_py_obj__(raw_branch, bkid, verified=True))
            except KeyError as error:
                raise KeyError( f'branch alias "{alias}" was not found in the list of '
                                f'branches aliases. Make sure you used a correct bkid. If'
                                 'you are sure of it, or did not input it yourself, '
                                 'it means it is not currently supported. Feel free to'
                                 'report it in order to improve this library.' ) from error
        return result
    
    @property
    def values(self) -> list[Branch]:
        return self._values

    @values.setter
    def values(self, *args, **kwargs) -> None:
        raise NotImplementedError()
    
    def __iter__(self):
        return iter(self._values)
    
    def __len__(self):
        return len(self._values)
    
    def __next__(self):
        return next(self._values)
    
    def __getitem__(self, __i: SupportsIndex, /):
        return self._values[__i]
    
    def __delitem__(self, __key: SupportsIndex | slice, /) -> None:
        return self._values.__delitem__(__key)
    
    def __setitem__(self, __key: SupportsIndex, __value: Any, /) -> None:
        return self._values.__setitem__(__key, __value)