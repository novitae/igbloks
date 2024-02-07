import pyparsing as pp
from typing import Any

__all__ = ( "deserialize", "serialize", )

# Définir les éléments de base du parser
LPAREN, RPAREN = map(pp.Suppress, "()")
number = pp.pyparsing_common.number
string = pp.QuotedString("\"", escChar='\\')
identifier = pp.Word(pp.alphas + ".", pp.alphanums + "_.")

# Définir les mots-clés pour "true", "false" et "null"
true = pp.Keyword("true").setParseAction(pp.replaceWith(True))
false = pp.Keyword("false").setParseAction(pp.replaceWith(False))
null = pp.Keyword("null").setParseAction(pp.replaceWith(None))

# Définir une référence avant pour les valeurs
value = pp.Forward()

# Définir les structures pour les tableaux
array = pp.Group(LPAREN + pp.Optional(pp.delimitedList(value)) + RPAREN)

# Définir ce que peut être une valeur
value << (true | false | null | number | string | identifier | array)

# Parser principal
parser = value

def deserialize(__s: str) -> list[str | int | bool | None | list]:
    return parser.parseString(__s, parseAll=True).asList()[0]

def serialize(__l: list[str | int | bool | None | list]) -> str:
    def serialize_item(item, i):
        if isinstance(item, str):
            return '"' + item.replace('"', '\\"') + '"' if i else item
        elif isinstance(item, bool):
            return 'true' if item else 'false'
        elif item is None:
            return 'null'
        elif isinstance(item, int):
            return str(item)
        elif isinstance(item, list):
            return '(' + ', '.join(serialize_item(item, x) for x, item in enumerate(item)) + ')'
        else:
            raise ValueError('Cannot serialize item of type ' + type(item).__name__)

    return serialize_item(__l, 0)

def find_json_encode_elements(data, *operands: str, found=None) -> list[list[str, Any]]:
    if found is None:
        found = []

    if isinstance(data, list) and len(data) >= 2:
        if data[0] in operands:
            found.append(data)
        else:
            for item in data:
                find_json_encode_elements(item, *operands, found=found)
    
    return found