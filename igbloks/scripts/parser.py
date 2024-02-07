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

def find_operands(script: list, *operands: str, found=None) -> list[list[str, Any]]:
    """Search for specific given operands.

    Args:
        script (list): The deserialized script to search in.
        *operands (str): The tuple of operands to search for. Defaults to None.

    Returns:
        list[list[str, Any]]: The list of matches, containing the full command \
            of with the operand in it.
    """
    if found is None:
        found = []

    if isinstance(script, list) and len(script) >= 2:
        if script[0] in operands:
            found.append(script)
        else:
            for item in script:
                find_operands(item, *operands, found=found)
    
    return found

def find_value(script: list, value: Any, returned_level: int = 1) -> list:
    """Searches for a given value inside a deserialized script.

    Args:
        script (list): The deserialized script.
        value (Any): The value to search for.
        returned_level (int, optional): The level relative to the value from \
            which we should return the value. Defaults to 1. Example:
            - "hi", 1:
            ```
            [
                3,
                "hi"
            ]
            ```
            - "hi", 2:
            ```
            [
                [
                    "uh"
                ],
                [
                    3,
                    "hi"
                ]
            ]
            ```
            - "hi", 3:
            ```
            [
                [
                    [
                        "uh"
                    ],
                    [
                        3,
                        "hi"
                    ]
                ],
                89,
                [
                    "bonjour"
                ]
            ]
            ```
    Returns:
        list: The value at its relative level.
    """
    # Fonction interne récursive avec chemin de suivi
    def recursive_search(lst, value, path):
        if value in lst:
            # Retourne le chemin mis à jour avec la position actuelle
            return path + [lst]
        for item in lst:
            if isinstance(item, list):
                result = recursive_search(item, value, path + [lst])
                if result is not None:
                    return result
        return None

    path_to_element = recursive_search(script, value, [])
    
    if path_to_element is None:
        return None  # L'élément n'a pas été trouvé
    
    # Remonte les niveaux en fonction de levels_to_go_up
    if returned_level >= len(path_to_element):
        # Si les niveaux à remonter dépassent la longueur du chemin, retourne la racine
        return path_to_element[0]
    else:
        # Sinon, retourne l'élément au niveau spécifié en remontant
        return path_to_element[-(returned_level + 1)]