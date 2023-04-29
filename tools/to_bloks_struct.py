import json

def merge_jsons(*jsons: dict):
    jsons_list, json = list(jsons), jsons[0]
    assert all([isinstance(json, item.__class__) for item in jsons_list])
    if isinstance(json, dict):
        result = {}
        for keys in zip(*map(lambda item: item.keys(), jsons_list)):
            values = [value[key] for key, value in list(zip(keys, jsons_list))]
            result["|".join(keys)] = merge_jsons(*values)
        return result
    elif isinstance(json, list):
        return [merge_jsons(*item) for item in zip(*jsons_list)]
    else:
        return json

def process_api_responses(responses: list[list[dict, dict]]) -> dict:
    result = {}

    def format_value(value: dict) -> dict:
        if isinstance(value, list):
            return [process_object(item) for item in value]
        elif isinstance(value, dict):
            return [process_object(value)]
        else:
            return [value]

    def process_object(obj: dict) -> str:
        name = list(obj.keys()).pop()
        values: dict = obj[name]

        if name not in result:
            result[name] = {}
        for key, value in values.items():
            if key not in result[name]:
                result[name][key] = {"types": [], "values": []}
            if (type_name := value.__class__.__name__) not in result[name][key]["types"]:
                result[name][key]["types"].append(type_name)
            result[name][key]["values"] += format_value(value)

        return name
    
    for response in responses:
        process_object(merge_jsons(*response))

    return result

with open("_raw_response_pairs.json", "r") as read:
    result = process_api_responses(json.load(read))

with open("_bloks_structure.json", "w") as f:
    json.dump(result, f, indent=4, sort_keys=True, ensure_ascii=False)