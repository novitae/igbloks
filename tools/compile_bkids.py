import json
from argparse import ArgumentParser
from pathlib import Path

from igbloks.utils import *

examples_path = Path(__file__).parent / "examples"

class BlokExplorer(dict[list[int], dict]):
    def _recurse(self, raw_branch: dict, indexes: list[int]) -> str:
        main_bn = branch_name(raw_branch)
        for str_index, branch in self.items():
            if main_bn in branch['aliases']:
                break
        else:
            str_index = "".join(map(str, indexes))
            if str_index not in self:
                self[str_index] = { "aliases": set(),
                                    "fields": {} }
        self[str_index]["aliases"].add(main_bn)

        def find_field(sub_index: int, is_list: bool = False) -> dict:
            if sub_index in self[str_index]["fields"]:
                return self[str_index]["fields"][sub_index]
            else:
                field = { "values": [],
                          "aliases": set(),
                          "is_list": is_list }
                self[str_index]["fields"][sub_index] = field
            return field

        # Accès aux valeurs de la branche
        for x, (key, value) in enumerate(raw_branch[main_bn].items()):
            # Branche
            if isinstance(value, dict):
                bn = self._recurse(value, indexes + [x])
                f = find_field(x)
                f["values"].append(f"class->{bn}")
            # Liste de branches
            elif isinstance(value, list):
                for y, sub_branch in enumerate(value):
                    bn = self._recurse(sub_branch, indexes + [x, y])
                    f = find_field(x, True)
                    f["values"].append(f"class->{bn}")
            # Autre
            else:
                f = find_field(x)
                f["values"].append(value)
            f["aliases"].add(key)
        return main_bn

    def explore(self, *args) -> list[dict]:
        for branch in args:
            self._recurse(branch, [0])
        result = []
        for value in self.values():
            value["fields"] = list(value["fields"].values())
            result.append(value)
        return result
    
def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("-f", "--files-path", nargs='+', default=[examples_path / f"bloks{x}.json" for x in [1, 2]])
    parser.add_argument("-n", "--export-name", default="merged")
    arguments = vars(parser.parse_args())

    datas = []
    for path in arguments.pop("files_path"):
        with open(path, "r") as read:
            datas.append(json.load(read))

    be = BlokExplorer()
    result = be.explore(*datas)
    
    def default(o: object):
        if isinstance(o, set):
            return list(o)

    with open(f"""{arguments.pop("export_name")}.json""", "w") as w:
        json.dump(
            result,
            w,
            indent=4,
            ensure_ascii=False,
            default=default
        )

if __name__ == "__main__":
    main()