from pyparsing import *
import re

__all__ = ( "raw_script_to_list", )

re_clean = re.compile(r',(?=\s*\))')
lparen = Suppress("(")
rparen = Suppress(")")
comma = Suppress(",")
string = QuotedString("\"", escChar='\\', unquoteResults=False)
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

def raw_to_list(__s: str) -> list[str | int | bool | None | list]:
    return parser.parseString(re_clean.sub('', __s)).asList()[0]
