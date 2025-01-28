from typing import Dict, Optional

class Tree:
    def __init__(self):
        pass

class BlokResponse:
    __slots__ = ("bloks_payload", "bkid")

    def __init__(
        self,
        bloks_payload: Dict,
        bkid: Optional[str] = None,
    ):
        assert isinstance(bloks_payload, dict), "`bloks_payload` must be of type `dict`"
        assert "tree" in bloks_payload, "key `'tree'` missing from dict `bloks_payload`"
        self.bloks_payload = bloks_payload

        assert bkid is None or isinstance(bkid, str), "`bkid` must be of type `str` or be `None`"
        self.bkid = bkid

    @classmethod
    def from_response_dict(cls, d: Dict, bkid: Optional[str] = None):
        assert isinstance(d, dict), "`d` should be dict obj"
        assert "layout" in d, "`d` doesn't contain any `'layout'` key"
        assert "bloks_payload" in d["layout"], "`d['layout']` doesn't contain any `'bloks_payload'`"
        return cls(bloks_payload=d["layout"]["bloks_payload"], bkid=bkid)