from typing import Any, Self, Callable, get_args, get_origin, Union
from types import GenericAlias, UnionType

from ..utils import *
from ..errors import *
from .types import BlokFieldType

__all__ = ( "MultipleAliasField", "BlokField", "Branch",
            "MultipleBranches", )

class BlokStrainer:
    def __init__(
        self,
        include_branches: set[str] = None,
        include_fields: set[str] = None,
        exclude_branches: str[str] = None,
        exclude_fields: str[str] = None,
        bkid: str = None,
        recursively: bool = True,
    ) -> None:
        pass

class MultipleAliasField:
    """
        `MultipleAliasField` is the base of `BlokField`, `Branch` and
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

    @classmethod
    def __to_py_obj__(
        cls,
        content: dict[str, dict[str, Any]],
        bkid: str,
        *,
        verified: bool = False,
    ) -> Self:
        ...

    def __to_bloks__(self, *args, **kwargs) -> dict:
        ...


class BlokField(MultipleAliasField):
    def __init__(
        self,
        aliases: dict[str, str],
        required: bool = False,
        default: Any = Undefined,
        default_factory: Callable[[], Any] = None,
        accepted_types: list[type | Self] = None,
        skip_type_verif: bool = False,
        is_list: bool = None,
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
            - `is_list` (`bool`): If the field contains a list of branches instead of a
                single branch. In this case, make sure all the possible types of the list
                are present in the type annotation as union. You can skip this field if
                you put all thoses types in a list, such as: `list[str | int | float]`.
        """
        super().__init__(aliases=aliases)

        self.required = required
        if default == Undefined and default_factory is None:
            pass
        elif default_factory is not None:
            if default != Undefined:
                raise ValueError( '`default` and `default_factory` arguments '
                                    'have been filled, so i don\'t know which to'
                                    ' use. Please fill only the one you want.' )
            elif callable(default_factory) is False:
                raise TypeError( '`default_factory` is not a callable' )
        else:
            default_factory = lambda: default
        self.default_factory = default_factory

        # Que fait-on:
        #   Required:
        #       Default:
        #           set defaut
        #       else:
        #           raise si pas présent
        #   Not required
        #       - fout sur undefined par défaut
        #       - not export if still undefined


        self.default_factory = default_factory

        self.is_list = False if is_list is None else is_list
        self.accepted_types = accepted_types
        self.skip_type_verif = skip_type_verif
        self.pretty_name = None

    def __repr__(self) -> str:
        return ( f"BlokField(required: {self.required}, "
                 f"accepted_types: {tuple(map(lambda item: item.__name__, self.accepted_types))}, "
                 f"is_list: {self.is_list}, "
                 f"aliases: {tuple(self.aliases.values())}, "
                 f"pretty_name: \"{self.pretty_name}\")" )
    
    @check_return_type
    def __to_py_obj__(self, content: Any, bkid: str, *args, **kwargs) -> Self:
        if is_branch_list(content):
            return [ self.__to_py_obj__( content=item,
                                         bkid=bkid,
                                         *args,
                                         verified=True,
                                         **kwargs ) for item in content ]
        if (branch_name := get_branch_name(content)) is not None:
            sub_branches = { item.aliases[bkid]: item for item in self.accepted_types
                             if issubclass(item, Branch) }
            if (matching_btype := sub_branches.get(branch_name)) is not None:
                return matching_btype.__to_py_obj__( content=content,
                                                     bkid=bkid,
                                                     verified=True )
        else:
            for blok_field_type in [ item for item in self.accepted_types
                                     if isinstance(item, BlokFieldType) ]:
                if blok_field_type.test_for(content) is True:
                    return blok_field_type.__to_py_obj__( content=content,
                                         bkid=bkid,
                                         *args,
                                         verified=True,
                                         **kwargs )
        if type(content) in self.accepted_types or content is Undefined:
            return content
        else:
            raise TypeError( 'no correct type adapter found' )

    @property
    def accepted_types(self) -> list[Self | type] | None:
        return self._accepted_types
    
    @accepted_types.setter
    def accepted_types(self, accepted_types: list[Self | type] | None) -> None:
        if accepted_types is not None:
            # Change list[str | tuple, int] to (str | tuple, <class 'int'>),
            # and overwrites the `is_list` attr.
            if isinstance(accepted_types, GenericAlias) and accepted_types.__name__ == "list":
                accepted_types = get_args(accepted_types)[0]
                self.is_list = True

            # str | tuple -> (str, tuple)
            if isinstance(accepted_types, UnionType): 
                accepted_types = accepted_types.__args__
            elif get_origin(accepted_types) == Union:
                accepted_types = get_args(accepted_types)

            # str -> (str, )
            elif isinstance(accepted_types, type):
                accepted_types = (accepted_types, )
            
            accepted_types = list(accepted_types)
            if Any in accepted_types:
                self.skip_type_verif = True

            if all([ item == Self or isinstance(item, type)
                     for item in accepted_types ]) is False:
                raise TypeError(f'a value of `accepted_types` is not a `type`: {accepted_types}')
            
        self._accepted_types = accepted_types

class Branch(MultipleAliasField):
    """
        Make sure to add a type to every fields, otherwise it won't
        be readen.
        - `aliases`: A dict of `bkid: name`
    """
    aliases: dict[str, str]

    def __init__(
        self,
        content: dict[str, dict[str, Any]],
        bkid: str,
        *args,
        verified: bool = False,
        **kwargs
    ) -> None:
        branch_name = get_branch_name(content)
        if verified is False and branch_name is None:
            raise InvalidRawBranchError( "invalid branch sent to class "
                                         f"`{self.__class__.__name__}`" )

        raw_fields = self.__class__.__annotations__.copy()
        if "aliases" in raw_fields:
            del raw_fields["aliases"]
        super().__init__(aliases=self.__class__.__dict__["aliases"])
        
        self.fields: dict[str, BlokField] = {}
        for field_name, field_types in raw_fields.items():
            field_infos: BlokField = self.__class__.__dict__[field_name]
            if isinstance(field_infos, BlokField) is False:
                raise TypeError( 'every field values must be instances of '
                                 '`BlokField` class (invalid found in branch'
                                f' "{self.__class__.__name__}")' )
            
            # Setting the accepted types, and changing Self to
            # self.__class__ so we can check for type instances
            if field_infos.accepted_types is None:
                field_infos.accepted_types = field_types
            if Self in field_infos.accepted_types:
                field_infos._accepted_types.remove(Self)
                field_infos._accepted_types.append(self.__class__)
            field_infos._accepted_types = tuple(field_infos._accepted_types)

            # Setting pretty name to find back the field
            if field_infos.pretty_name is None:
                field_infos.pretty_name = field_name
            self.fields[field_name] = field_infos

            # Finding appropriate values in the input content,
            # loading them and setting them as attributes
            field_value = content[branch_name].get(field_infos.aliases[bkid], Undefined)
            self.__setattr__(field_name, field_value, bkid=bkid, *args, **kwargs)
            
    def __setattr__(
        self,
        field_name: str,
        field_value: Any,
        bkid: str = None,
        *args,
        **kwargs
    ) -> None:
        if hasattr(self, 'fields') and field_name in self.fields:
            field_infos = self.fields[field_name]
            if field_value is Undefined:
                if field_infos.required:
                    try:
                        field_value = field_infos.default_factory()
                    except TypeError as error:
                        raise MissingDefaultBuilderError(
                            f'field `{field_infos.pretty_name}` from branch `'
                            f'{self.__class__.__name__}` was not set correctly,'
                            ' but was required. Not finding a value for this '
                            'field resulted a miss of a value to place as an '
                            'attribute for the field.' ) from error
            else:
                field_value = field_infos.__to_py_obj__( content=field_value,
                                                         bkid=bkid,
                                                         *args,
                                                         **kwargs, )

        return super().__setattr__(field_name, field_value)
    
    def __repr__(self) -> str:
        content = {key: self.__getattribute__(key) for key in self.fields.keys()}
        content = ", ".join(f"{key}: {repr(value)}" for key, value in content.items() if value != Undefined)
        return f"{self.__class__.__name__}({content})"
    
    @classmethod
    def __to_py_obj__(
        cls,
        content: dict[str, dict[str, Any]],
        bkid: str,
        *args,
        verified: bool = False,
        **kwargs,
    ) -> Self:
        return cls(
            content=content,
            bkid=bkid,
            *args,
            verified=verified,
            **kwargs
        )

    def __to_bloks__(self, *args, **kwargs) -> dict:
        ""

# Need to do the list support