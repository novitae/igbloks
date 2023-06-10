import json
from pydantic import BaseModel, Field
from pathlib import Path
from typing import Any
from argparse import ArgumentParser

from igbloks.utils import *

# - The input directory must be a directory full of bloks tree.
# - Their name must contain the blokid of their request. I suggest
#   using `{app name}|{bkid}.json` as a name. See ./examples/tree_compiler

class AliasesModel(BaseModel):
    aliases: dict[str, str] = {}
    indexes_path: list[list[int]] = Field([], exclude=True)

    def set_alias(
        self,
        bkid: str,
        alias: str,
    ) -> None:
        if self.aliases.get(bkid) != alias:
            for key, value in self.aliases.items():
                if value == alias:
                    self.aliases[bkid] = f"-same-as->{key}"
                    break
            else:
                self.aliases[bkid] = alias

class BlokField(AliasesModel):
    values: list = []
    is_list: bool = False

    def append_value(self, bkid: str, value: Any, bc: "BlokClasses", index_path: list[int]):
        if isinstance(value, list):
            self.values += [f"-class->" + get_branch_name(item) for item in value]
            self.is_list = True
            recurse((bkid, value), index_path=index_path, bc=bc)
        elif isinstance(value, dict):
            self.values.append(f"-class->" + get_branch_name(value))
            recurse((bkid, value), index_path=index_path, bc=bc)
        else:
            self.values.append(value)

class BlokClass(AliasesModel):
    fields: list[BlokField] = []

    def field_name(
        self,
        bkid: str,
        alias: str,
        index_path: list[int],
    ) -> str:
        for field_index, value in enumerate(self.fields):
            if ( alias in value.aliases.values() or
                 index_path in value.indexes_path ):
                self.fields[field_index].indexes_path.append(index_path)
                self.fields[field_index].set_alias(bkid, alias)
                return field_index
        else:
            field_index = len(self.fields)
            self.fields.append(BlokField())
            self.fields[field_index].indexes_path.append(index_path)
            self.fields[field_index].set_alias(bkid, alias)
            return field_index
        
class BlokClasses(BaseModel):
    classes: list[BlokClass] = []

    def class_name(
        self,
        bkid: str,
        alias: str,
        index_path: list[int],
    ) -> str:
        for class_index, value in enumerate(self.classes):
            if ( alias in value.aliases.values()
                 or index_path in value.indexes_path ):
                self.classes[class_index].indexes_path.append(index_path)
                self.classes[class_index].set_alias(bkid, alias)
                return class_index
        else:
            class_index = len(self.classes)
            self.classes.append(BlokClass())
            self.classes[class_index].indexes_path.append(index_path)
            self.classes[class_index].set_alias(bkid, alias)
            return class_index
        
def recurse(
    *datas: tuple[str, dict],
    index_path: list[int] = [0],
    bc: BlokClasses = BlokClasses(),
) -> BlokClasses:
    if all([is_branch(data[1]) for data in datas]):
        # print("All branches")
        for bkid, raw_blok in datas:
            bn = get_branch_name(raw_blok)
            saved_bn = bc.class_name(bkid, bn, index_path)
            for field_index, (field_key, field_value) in enumerate(raw_blok[bn].items()):
                fn = bc.classes[saved_bn].field_name(bkid, field_key, index_path + [field_index])
                bc.classes[saved_bn].fields[fn].append_value(bkid, field_value, bc, index_path + [field_index])
        return bc
    elif all([is_branch_list(data[1]) for data in datas]):
        # datas = tuple((bkid: list(branch)))
        for values_index, values in enumerate(zip(*[data[1] for data in datas])):
            values = list(zip([data[0] for data in datas], values))
            recurse(*values, index_path=index_path + [values_index], bc=bc)
        # print("All branches list")
    else:
        print("Not found", datas)

def main():
    parser = ArgumentParser()
    parser.add_argument("-d", "--directory", default=None)
    parser.add_argument("-n", "--name", default="merged")
    arguments = vars(parser.parse_args())

    directory = Path(ad) if (ad := arguments.get("directory")) else Path(__file__).parent / "examples" / "tree_compiler"
    paths = list(directory.glob("*.json"))
    datas = []
    for path in paths:
        with open(path, "r") as read:
            datas.append(json.load(read))

    result = recurse(*zip(map(lambda item: item.stem.split("|")[-1].strip(), paths), datas))

    def defaut(o: object):
        if isinstance(o, BaseModel):
            return o.dict(exclude={'indexes_path'})
        elif isinstance(o, set):
            return list(o)
        
    with open(f"""{arguments["name"]}.json""", "w") as write:
        json.dump(
            result,
            write,
            indent=4,
            default=defaut,
            ensure_ascii=False
        )

if __name__ == "__main__":
    main()