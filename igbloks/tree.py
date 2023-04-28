_ios_bkv = "55982b30b2731b78bf0838812a891c66e9715e1dcb4be18cc55a9772809153cc"
_web_bkv = "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6"

class BKVMatches(dict):
    def __setitem__(self, __key: str | bytes, __value: str) -> None:
        if isinstance(__key, bytes):
            __key = __key.hex()
        if not isinstance(__key, str):
            raise TypeError( f"`__key` must be of `str` type, not {__key.__class__}" )
        if (lk := len(__key)) != 64:
            raise ValueError( f"`__key` must be of `64` long `str`, not {lk}" )
        return super().__setitem__(__key, __value)
    
    @classmethod
    def correct_init(
        cls,
        ios: str = None,
        web: str = None,
    ) -> "BKVMatches":
        result = cls()
        for key, value in zip([_ios_bkv, _web_bkv], [ios, web]):
            if value is not None:
                result[key] = value
        return result

class Branch:
    __bkv_matches: BKVMatches = BKVMatches.correct_init("㐈", "bk.components.Flexbox")

branches = [item for item in locals().values() if hasattr("__bkv_matches", item)]

branches_dict: dict[str, Branch] = {}
for _branch in branches:
    for _n in _branch.__bkv_matches.values():
        branches_dict[_n] = _branch
else:
    del _branch, _n

