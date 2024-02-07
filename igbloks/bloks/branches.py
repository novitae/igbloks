from typing import Any, Self

class BlokBuilder:
    def __init__(
        self,
        aliases: dict[str, list[str]] = None,
    ) -> None:
        self.aliases = aliases or {}

    def add_bkid_alias(
        self,
        bkid: str,
        alias: str,
    ) -> None:
        """Add an alias for the field key for a certain bkid.

        Args:
            bkid (str): The bkid.
            alias (str): The field alias for the bkid.
        """
        if alias not in self.aliases:
            self.aliases[alias] = []
        self.aliases[alias].append(bkid)

class BlokFieldBuilder(BlokBuilder):
    def __init__(
        self,
        aliases: dict[str, list[str]] = None,
        values: list[Any] = None,
        required: bool = None,
        is_list: bool = None
    ) -> None:
        super().__init__(aliases=aliases)
        self.values = values or []
        self.required = required or False
        self.is_list = is_list or False

    def __repr__(self) -> str:
        return f"BlokFieldBuilder({list(self.aliases.keys())}, required: {self.required}, is_list: {self.is_list})"

    @property
    def bkids(self) -> list[str]:
        """Returns the list of bkid of the field."""
        result = []
        for value in self.aliases.values():
            result += value
        return result

    def add_bkid_alias_value(
        self,
        bkid: str,
        alias: str,
        value: Any,
    ) -> None:
        """Add an alias for the field key for a certain bkid, and its value.

        Args:
            bkid (str): The bkid.
            alias (str): The field alias for the bkid.
            value (value): The value of the field.
        """
        self.add_bkid_alias(bkid=bkid, alias=alias)
        self.add_value(value=value)

    def add_value(
        self,
        value: Any
    ) -> None:
        """Add a value to the field.

        Args:
            value (value): The value of the field.
        """
        self.values.append(value)

    def update(
        self,
        field: Self,
    ) -> None:
        self_aliases = list(enumerate(self.aliases))
        for alias, bkids in field:
            for i, (x, (self_alias, self_bkids)) in enumerate(self_aliases):
                if alias == self_alias:
                    for bkid in bkids:
                        if bkid not in self_bkids:
                            self.aliases[x].append(bkid)
                    del self_aliases[i]

    def __len__(self) -> int:
        return len(self.aliases)

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, self.__class__):
            less_aliases, most_aliases = sorted([self, __value], key=len)
            for alias, bkids in less_aliases.aliases.items():
                # If one of the alias is in the other aliases
                if alias in most_aliases.aliases:
                    # We check if at least one bkid is matching
                    # with the other aliases of the bkid.
                    other_bkids = most_aliases.aliases[alias]
                    for bkid in bkids:
                        if bkid in other_bkids:
                            return True
        return False
    
    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)

class BlokObjectBuilder(BlokBuilder):
    def __init__(
        self,
        aliases: dict[str, list[str]] = None,
        fields: list[BlokFieldBuilder] = None,
    ) -> None:
        super().__init__(aliases=aliases)
        self.fields = fields or []

    def __repr__(self) -> str:
        return f"""BlokObjectBuilder(aliases: {list(self.aliases.keys())}, fields: {self.fields})"""

    def add_field(
        self,
        field: BlokFieldBuilder,
    ) -> None:
        for x, self_field in enumerate(self.fields):
            if field == self_field:
                self.fields[x].update(field)
                break
        else:
            self.fields.append(field)