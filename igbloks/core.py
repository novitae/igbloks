from typing import Dict, Optional, Any, Union
from pydantic.dataclasses import dataclass
from pydantic import field_validator, Field
import orjson

class Tree:
    def __init__(self):
        pass

@dataclass(frozen=True)
class BlokResponse:
    bloks_payload: Dict
    """The `'bloks_payload'` element."""

    bkid: Optional[str] = Field(pattern=r"^[a-f\d]{64}$")
    """The blok id of the response."""

    @field_validator('bloks_payload', mode='before')
    def validate_bloks_payload(cls, v: Any):
        assert isinstance(v, dict), "`bloks_payload` must be of type `dict`"
        assert "tree" in v, "key `'tree'` missing from dict `bloks_payload`"
        return v
    
    @classmethod
    def from_app_response_dict(cls, d: Dict, *, bkid: Optional[str] = None):
        assert isinstance(d, dict), "`d` should be dict obj"
        assert "layout" in d, "`d` doesn't contain any `'layout'` key"
        assert "bloks_payload" in d["layout"], "`d['layout']` doesn't contain any `'bloks_payload'`"
        return cls(bloks_payload=d["layout"]["bloks_payload"], bkid=bkid)
    
    @classmethod
    def from_app_response(cls, t: Union[bytes, str], *, bkid: Optional[str] = None):
        return cls.from_app_response_dict(d=orjson.loads(t), bkid=bkid)
    
    @classmethod
    def from_web_response(cls, t: Union[bytes, str], *, bkid: Optional[str] = None):
        if isinstance(t, str):
            t = t.encode()
        else:
            assert isinstance(t, bytes), "Argument `t` must be of type `str` or `bytes`"
        raw_dict = orjson.loads(t.removeprefix(b"for (;;);"))
        assert (payload := raw_dict.get("payload")) is not None, "Key `'payload'` is missing from the dict in `t`"
        assert (layout := payload.get("layout")) is not None, "Key `'layout'` is missing from the dict in `t['payload']`"
        assert (bloks_payload := layout.get("bloks_payload")) is not None, "Key `'bloks_payload'` is missing from the dict in `t['payload']['layout']`"
        return cls(bloks_payload=bloks_payload, bkid=bkid)