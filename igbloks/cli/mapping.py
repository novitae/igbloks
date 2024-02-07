from pathlib import Path
import json

from ..utils import is_branch, is_branch_list, get_branch_name
from ..bloks.branches import BlokFieldBuilder, BlokObjectBuilder

class MappingCache(list[BlokObjectBuilder]): pass

_excluded_values = [], {}

def recursion_mapping(
    mapping_cache: MappingCache,
    branches: dict[str, dict],
) -> BlokObjectBuilder:
    blok_object = BlokObjectBuilder()
    class_names, blok_ids = [], []
    for bkid, branch in branches.items():
        assert is_branch(branch)
        branch_name = get_branch_name(branch, verified_branch=True)

        class_names.append(branch_name)
        blok_ids.append(bkid)
        blok_object.add_bkid_alias(bkid, branch_name)

    datas = []
    for bkid, class_name in zip(blok_ids, class_names):
        datas.append([ (key, value) for key, value
                       in branches[bkid][class_name].items()
                       if value not in _excluded_values ])

    length = len(datas[0])
    mapping_cache.append(blok_object)
    if not all(len(data) == length for data in datas[1:]):
        return blok_object

    for i in range(length):
        field = BlokFieldBuilder()
        specific_i_data = [data[i] for data in datas]
        # specific_i_data = [
        #   [alias_key, object[alias_objname, {objvalue}]],
        #   [alias_key, object[alias_objname, {objvalue}]]
        # ]

        value_object = specific_i_data[0][1]
        _is_branch = is_branch(value_object)
        _is_brlist = is_branch_list(value_object)

        if _is_branch or _is_brlist:
            if _is_branch:
                value = recursion_mapping( mapping_cache=mapping_cache,
                                           branches=dict(zip(blok_ids, [item[1] for item in specific_i_data])), )
                for x, key in enumerate([item[0] for item in specific_i_data]):
                    field.add_bkid_alias_value(blok_ids[x], key, value)

            else:
                field.is_list = True
                print("list, skip")

        else:
            for x, (key, value) in enumerate(specific_i_data):
                field.add_bkid_alias_value(blok_ids[x], key, value)

        blok_object.add_field(field)
    
    return blok_object

def schema_for_appid(path: str | Path):
    if isinstance(path, str):
        path = Path(path)
        assert path.exists()

    mapping_cache = MappingCache()
    payloads = {}

    for p in path.glob("*.json"):
        bkid = p.stem

        with open(p, "r") as read:
            payload = json.load(read)
        payloads[bkid] = payload["layout"]["bloks_payload"]["tree"]

    recursion_mapping(mapping_cache, payloads)
    return mapping_cache