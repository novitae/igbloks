from pyparsing import *
import re

__all__ = ( "deserialize", "serialize", )

re_clean = re.compile(r',(?=\s*\))')
lparen = Suppress("(")
rparen = Suppress(")")
comma = Suppress(",")
string = string = QuotedString("\"", escChar='\\', unquoteResults=False).setParseAction(lambda t: t[0][1:-1].encode('utf-8').decode('unicode_escape'))
identifier = Word(alphas + ".", alphanums + "_.")
unicode_string = Combine(Literal("\\u") + Word(hexnums, exact=4)).setParseAction(lambda t: chr(int(t[0][2:], 16)))
number = Word(nums).setParseAction(lambda t: int(t[0]))
boolean = (Keyword("true") | Keyword("false")).setParseAction(lambda t: t[0] == "true")
null = Keyword("null").setParseAction(lambda t: None)
value = Forward()
array = Group(lparen + Optional(delimitedList(value)) + rparen)
value << (unicode_string | string | identifier | number | boolean | null | array)
parser = OneOrMore(value)
parser = parser.leaveWhitespace()

def deserialize(__s: str) -> list[str | int | bool | None | list]:
    return parser.parseString(re_clean.sub('', __s)).asList()[0]

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