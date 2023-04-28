import json

def analyse_bloks(compressed_bloks, readable_bloks, parent_key=None, result=None):
    if result is None:
        result = {}

    if isinstance(compressed_bloks, dict) and isinstance(readable_bloks, dict):
        for (c_key, c_value), (r_key, r_value) in zip(compressed_bloks.items(), readable_bloks.items()):
            full_key = f"{r_key}|{c_key}"
            if parent_key is not None:
                if parent_key not in result:
                    result[parent_key] = {}
                if full_key not in result[parent_key]:
                    result[parent_key][full_key] = {'values': [], 'types': set()}
                if not isinstance(c_value, (list, dict)):
                    if c_value not in result[parent_key][full_key]['values']:
                        result[parent_key][full_key]['values'].append(c_value)
                result[parent_key][full_key]['types'].add(type(c_value).__name__)
            if isinstance(c_value, dict) and isinstance(r_value, dict):
                first_c_key = list(c_value.keys())[0]
                first_r_key = list(r_value.keys())[0]
                analyse_bloks(c_value, r_value, full_key, result)
                if parent_key:
                    result[parent_key][full_key]['values'].append(f"{first_r_key}|{first_c_key}")
            elif isinstance(c_value, list) and isinstance(r_value, list):
                analyse_bloks(c_value, r_value, full_key, result)
    elif isinstance(compressed_bloks, list) and isinstance(readable_bloks, list):
        for c_item, r_item in zip(compressed_bloks, readable_bloks):
            analyse_bloks(c_item, r_item, parent_key, result)
    return result

def process_api_responses(api_responses):
    result = {}
    for compressed_bloks, readable_bloks in api_responses:
        result.update(analyse_bloks(compressed_bloks, readable_bloks))
    return result

with open("raw_response_pairs.json", "r") as read:
    result = process_api_responses(json.load(read))

def default(o: object):
    if isinstance(o, (tuple, set)):
        return list(o)

with open("bloks_structure.json", "w") as f:
    json.dump(result, f, indent=4, sort_keys=True, default=default, ensure_ascii=False)