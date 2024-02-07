from io import StringIO, BufferedWriter

from .utils import is_branch, is_branch_list

class ConvertableBranchList(list["ConvertableBranch"]):
    def __repr__(self) -> str:
        return "ConvertableBranchList[%s]" % ", ".join(map(repr, self))

class ConvertableBranch:
    def __init__(self, branch: dict, recursive: bool = True) -> None:
        for name, content in branch.items():
            break
        self.name = name
        if recursive is False:
            self.content = content
        else:
            self.content = {}
            for key, value in content.items():
                if is_branch(value):
                    value = ConvertableBranch(value, recursive=recursive)
                elif is_branch_list(value):
                    value = ConvertableBranchList([ConvertableBranch(item, recursive=recursive) for item in value])
                self.content[key] = value

    def __repr__(self) -> str:
        return f"ConvertableBranch({self.name}, {self.content})"
    
    def _opening_separator(self, as_hex: bool = False) -> str:
        attrs = [ f"""{("x" + name.encode().hex().upper()) if as_hex else name}='{value}'"""
                  for name, value in self.content.items()
                  if isinstance(value, (ConvertableBranch, ConvertableBranchList)) is False ]
        return "<%s%s>" % (("x" + self.name.encode().hex().upper() if as_hex else self.name), (" " + attrs_ if (attrs_ := " ".join(attrs)) else ""))
    
    def _closing_separator(self, as_hex: bool = False) -> str:
        return f"</x{self.name.encode().hex().upper() if as_hex else self.name}>"
    
    def _dumps(self, indent: int, level: int, as_hex: bool = False) -> str:
        result = ""
        l = len(self.content) - 1
        for x, (name, value) in enumerate(self.content.items()):
            name = "x" + name.encode().hex().upper() if as_hex else name
            opening = f"<{name}>"
            closing = f"</{name}>"
            if isinstance(value, ConvertableBranch) is True:
                value = ConvertableBranchList([value])
            if isinstance(value, ConvertableBranchList) is True:
                data = [branch.dumps(indent=indent, as_hex=as_hex, level=level + 1) for branch in value]
                if indent > 0:
                    opening = ((indent * level) * " ") + opening + "\n"
                result += opening
                result += "".join(data)
                if indent > 0:
                    closing = ((indent * level) * " ") + closing + ("\n" if x != l else "")
                result += closing
        return result

    def dump(self, buffer: BufferedWriter, indent: int = 0, as_hex: bool = False, *, level: int = 0) -> None:
        opening = self._opening_separator(as_hex=as_hex)
        dumped = self._dumps(indent=indent, level=level + 1, as_hex=as_hex)
        has_content = dumped.strip()
        if indent > 0:
            opening = ((indent * level) * " ") + opening + ("\n" if has_content else "")
        buffer.write(opening)
        buffer.write(dumped)
        closing = self._closing_separator(as_hex=as_hex)
        if indent > 0:
            closing = (("" if dumped.endswith("\n") else "\n") + ((indent * level) * " ") if has_content else "") + closing + "\n"
        buffer.write(closing)

    def dumps(self, indent: int = 0, as_hex: bool = False, *, level: int = 0):
        buffer = StringIO()
        self.dump(buffer=buffer, indent=indent, as_hex=as_hex, level=level)
        return buffer.getvalue()
    
def bloks_to_html(tree: dict, indent: int = 0, as_hex: bool = False) -> str:
    """Turns a tree payload into HTML

    Args:
        tree (dict): The data at ["layout"]["bloks_payload"]["tree"]
        as_hex (bool): Export the keys as hex. Default to False.
        indent (int, optional): The indent level. Defaults to 0.

    Returns:
        str: The HTML.
    """
    assert is_branch(tree), 'tree is not a branch, make sure you are placing the value at ["layout"]["bloks_payload"]["tree"]'
    return ConvertableBranch(tree, recursive=True).dumps(indent=indent, as_hex=as_hex)