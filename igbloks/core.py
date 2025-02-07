from typing import Dict, Optional, Any, Union, List
from pydantic.dataclasses import dataclass
from pydantic import field_validator, Field
import orjson

from .scripts.parser import parse_script, PARSED_FUNCTION

__all__ = ("BlokResponse", )

# from .tree import Tree

# It might be possible that the `async_action` has only `action` instead of `tree`,
# And that `app` has only tree.

@dataclass(frozen=True)
class ErrorAttribution:
    logging_id: str
    '''The `logging_id` dict. 
    
    It looks like:
    ```json
    {"callsite":"{\\"product\\":\\"two_step_verification\\",\\"feature\\":\\"com.bloks.www.two_step_verification.has_been_allowed.async\\",\\"integration\\":\\"bloks_screen\\",\\"oncall\\":\\"two_step_verification\\"}\","push_phase":"C3","version":1,"request_id":"An5-hk5WYC9RwS1TKJvGer-","www_revision":1019852061}"
    ```

    Its json-loaded value can be accessed by using `.logging_id_callsite`.
    '''
    source_map_id: str
    """The `source_map_id` string."""

    @property
    def logging_id_loaded(self) -> Dict[str, Dict[str, Union[str, int]]]:
        if hasattr(self, "_logging_id_loaded") is False:
            loaded_logging_id = orjson.loads(self.logging_id)
            loaded_logging_id["callsite"] = orjson.loads(loaded_logging_id["callsite"])
            object.__setattr__(self, "_logging_id_loaded", loaded_logging_id)
        return self._logging_id_loaded
    
    @property
    def product(self) -> str:
        return self.logging_id_loaded["callsite"]["product"]
    
    @property
    def feature(self) -> str:
        return self.logging_id_loaded["callsite"]["feature"]
    
    @property
    def version(self) -> int:
        return self.logging_id_loaded["version"]
    
    @property
    def request_id(self) -> str:
        return self.logging_id_loaded["request_id"]

@dataclass(frozen=True)
class BloksPayload:
    data: List
    """The list of variables."""

    error_attribution: ErrorAttribution
    """The `error_attribution` object."""

    ft: Dict[str, str] = None
    """Custom functions map."""

    @property
    def functions(self) -> Dict[str, PARSED_FUNCTION]:
        """Returns the `ft` dict but the contained functions are parsed.

        Returns:
            Dict[str, PARSED_FUNCTION]: The `ft` with parsed functions.
        """
        if hasattr(self, "_functions") is False:
            object.__setattr__(
                self, "_functions",
                {
                    key: parse_script(value) for key, value in
                    ([] if self.ft is None else self.ft.items())
                }
            )
        return self._functions
    
    # @property
    # def variables()

class ActionBloksPayload(BloksPayload):
    action: str
    """The action to perform"""

@dataclass(frozen=True)
class BlokResponse:
    bloks_payload: BloksPayload
    """The `'bloks_payload'` element."""

    bkid: Optional[str] = Field(pattern=r"^[a-f\d]{64}$")
    """The blok id of the response."""

    @field_validator('bloks_payload', mode='before')
    def validate_bloks_payload(cls, v: Any):
        assert isinstance(v, dict), "`bloks_payload` must be of type `dict`"
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