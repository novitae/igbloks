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
        """Returns a `BlokResponse` object for the dict in a response from the api bloks endpoint of
            instagram (https://i.instagram.com/api/v1/bloks/apps/.../).

        Args:
            d (Dict): The dict inside of the response.
            bkid (Optional[str], optional): The blok id used in the response's request. Defaults to None.
        
        Raises:
            AssertionError: The argument `d` isn't a `dict`.
            KeyError: The dict `d` has missing keys.

        Returns:
            BlokResponse: The initialized `BlokResponse` object.
        """
        assert isinstance(d, dict), "`d` should be dict obj"
        return cls(bloks_payload=d["layout"]["bloks_payload"], bkid=bkid)
    
    @classmethod
    def from_app_response(cls, t: Union[bytes, str], *, bkid: Optional[str] = None):
        """Returns a `BlokResponse` object for the body of a response from the api bloks endpoint of
            instagram (https://i.instagram.com/api/v1/bloks/apps/.../).

        Args:
            t (Union[bytes, str]): The body of the response.
            bkid (Optional[str], optional): The blok id used in the response's request. Defaults to None.

        Raises:
            AssertionError: The JSON-loaded content of `t` isn't a `dict`.
            KeyError: The JSON-loaded dict from `t` has missing keys.

        Returns:
            BlokResponse: The initialized `BlokResponse` object.
        """
        return cls.from_app_response_dict(d=orjson.loads(t), bkid=bkid)
    
    @classmethod
    def from_web_response(cls, t: Union[bytes, str], *, bkid: Optional[str] = None):
        """Returns a `BlokResponse` object for the body of a response from the web bloks endpoint of
            instagram (https://www.instagram.com/async/wbloks/fetch/).

        Args:
            t (Union[bytes, str]): The body of the response.
            bkid (Optional[str], optional): The blok id used in the response's request. Defaults to None.

        Raises:
            AssertionError: The type of `t` isn't a `str` or `bytes`.
            KeyError: The `dict` inside of `t` has missing keys.

        Returns:
            BlokResponse: The initialized `BlokResponse` object.
        """
        if isinstance(t, str):
            t = t.encode()
        else:
            assert isinstance(t, bytes), "Argument `t` must be of type `str` or `bytes`"
        raw_dict = orjson.loads(t.removeprefix(b"for (;;);"))
        return cls(bloks_payload=raw_dict["payload"]["layout"]["bloks_payload"], bkid=bkid)
    
    @classmethod
    def from_graphql_response(cls, t: Union[bytes, str], *, bkid: Optional[str] = None):
        """Returns a `BlokResponse` object for the body of a bloks response from the graphql endpoint
            of instagram (https://i.instagram.com/graphql_www).

        Args:
            t (Union[bytes, str]): The body of the response.
            bkid (Optional[str], optional): The blok id used in the response's request. Defaults to None.

        Raises:
            AssertionError: The type of `t` isn't a `str` or `bytes`.
            KeyError: The `dict` inside of `t` has missing keys.

        Returns:
            BlokResponse: The initialized `BlokResponse` object.
        """
        if isinstance(t, str):
            t = t.encode()
        else:
            assert isinstance(t, bytes), "Argument `t` must be of type `str` or `bytes`"
        raw_dict = orjson.loads(t)
        return cls.from_app_response(
            t=raw_dict["data"]["1$bloks_app(bk_context:$bk_context,params:$params)"]\
                      ["screen_content"]["component"]["bundle"]["bloks_bundle_tree"],
            bkid=bkid,
        )
    
    @classmethod
    def from_response(cls, t: Union[bytes, str], *, bkid: Optional[str] = None):
        """Returns a `BlokResponse` object from the raw body of a bloks response. It will automatically
            detect where it comes from (between api, web or graphql).

        Args:
            t (Union[bytes, str]): The body of the response.
            bkid (Optional[str], optional): The blok id used in the response's request. Defaults to None.

        Raises:
            AssertionError: The type of `t` isn't a `str` or `bytes`.
            KeyError: The `dict` inside of `t` has missing keys.
            ValueError: Could not find what is the response type.

        Returns:
            BlokResponse: The initialized `BlokResponse` object.
        """
        if isinstance(t, str):
            t = t.encode()
        else:
            assert isinstance(t, bytes), "Argument `t` must be of type `str` or `bytes`"
        if t.startswith(b"for (;;);"):
            return cls.from_web_response(t=t, bkid=bkid)
        elif t.removeprefix(b"{").lstrip().startswith(b'"data":'):
            return cls.from_graphql_response(t=t, bkid=bkid)
        elif t.removeprefix(b"{").lstrip().startswith(b'"layout":'):
            return cls.from_app_response(t=t, bkid=bkid)
        else:
            raise ValueError('Could not find what is the response type.')