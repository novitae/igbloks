import json

flat_json_dumps = lambda item: json.dumps(item, separators=(",", ":"))

def export_recursive_zip(*items) -> list[dict]:
    classes = []

    def _rec_zip(*items, is_value: bool = False):
        first_value = items[0]
        assert all([isinstance(first_value, item.__class__) for item in items[1:]])
        if isinstance(first_value, dict):
            result = {}
            zip_result = list(zip(*[item.items() for item in items]))
            for zippeds in zip_result:
                result[flat_json_dumps(_rec_zip(*[zipped[0] for zipped in zippeds]))] = _rec_zip(*[zipped[1] for zipped in zippeds], is_value=True)
            return result
        elif isinstance(first_value, list):
            return [_rec_zip(*items) for items in zip(*items)]
        else:
            return type(first_value).__name__ if is_value else list(items)
    return _rec_zip(*items)
        
with open("ios.json", "r") as read:
    ios = json.load(read)

with open("web.json", "r") as read:
    web = json.load(read)

with open("merge.json", "w") as write:
    json.dump(export_recursive_zip(web, ios), write, indent=4)
