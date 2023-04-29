import json

# se méfier du "㐵|flex"

def decompose_name(name: str) -> tuple[str, str]:
    return tuple(sorted(name.split('|'), key=lambda item: len(item)))

def create_pydantic(data: dict[str, dict]) -> str:
    result = [
        "from pydantic import BaseModel, Field, validator\n",
        "class Branch(BaseModel):",
        "    @validator('*', pre=True)",
        "    def validate(cls, value):",
        "        return value",
        "",
        "class _UnSet: pass",
        "UnSet = _UnSet()",
        "",
    ]

    for object_name, object_fields in data.items():
        short_on, long_on = decompose_name(object_name)
        class_name = long_on.replace(".", "_")
        result.append(f"""class {class_name}__{short_on}(Branch):""")

        to_validate: list[tuple[str, str]] = []

        for field_name, field_attrs in object_fields.items():
            short_fn, long_fn = decompose_name(field_name)
            is_list = field_attrs["types"][0] == "list"
            if field_attrs["types"][0] in ["list", "dict"]:
                raw_ftypes = list(set(map(lambda item: decompose_name(item), field_attrs["values"])))
                field_types = list(map(lambda item: item[1].replace(".", "_") + "__" + item[0], raw_ftypes)) or field_attrs["types"]
            else:
                field_types = field_attrs["types"]
            field_types_str = " | ".join(field_types)
            field_types_str = f"list[{field_types_str}]" if is_list else field_types_str
            result.append(f"""    {long_fn}: {field_types_str} = Field(UnSet, alias='{short_fn}')""")

            if len(field_types) > 1:
                to_validate.append((long_fn, raw_ftypes, is_list))
        
        if to_validate:
            result.append(f"""\n    @validator({", ".join([f"'{name[0]}'" for name in to_validate])}, pre=True)""")
            result.append("    def validate(cls, value) -> Branch:")

            result.append("        def find_type(v):")
            for x, (_, varn, is_list) in enumerate(to_validate):
                for short_varn, long_varn in varn:
                    result.append(f"""            {"elif" if x else "if"} '{short_varn}' in v:""")
                    cls_nm = f"""{long_varn.replace(".", "_")}__{short_varn}"""
                    if is_list:
                        result.append(f"""                return [{cls_nm}(**item) for item in v]""")
                    else:
                        result.append(f"""                return {cls_nm}(**v)""")

            result.append(f"""            else:\n                raise ValueError(f'class not found for {{v}}')\n""")
            result.append('        return find_type(value)')
        result.append("")

    return "\n".join(result)

with open("_bloks_structure.json", "r") as f:
    bloks_data = json.load(f)

with open("pyd.py", "w") as write:
    write.write(create_pydantic(bloks_data))