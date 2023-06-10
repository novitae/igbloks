from typing import Any, Self
from pydantic import BaseModel, Field
from enum import Enum
import re

from ..utils import rgb_to_hex, hex_to_rgb, enum_list

__all__ = (
    "BlokFieldType",
    "DifferentDirection", "Direction",
    "DifferentAlignment", "Alignment",
    "DifferentJustify", "Justify",
    "SizeUnits", "DisplaySize",
    "DifferentTextStyle", "TextStyle",
    "RGB_or_RGBA_Color",
    "URL",
    "TextSize",
)

class BlokFieldType(BaseModel):
    @classmethod
    def test_for(cls, value: Any) -> bool:
        ...

    @classmethod
    def __to_py_obj__(cls, value: Any, *, verified: bool = False) -> Self:
        if verified is False:
            assert cls.test_for(value)
        return value

    def __to_bloks__(self, *args, **kwargs) -> dict:
        ...

class DifferentDirection(str, Enum):
    """Different directions"""
    row: str = "row"
    column: str = "column"
_direction_strict = enum_list(DifferentDirection)
class Direction(BlokFieldType):
    """Field type for direction"""
    direction: DifferentDirection

    @classmethod
    def test_for(cls, value: Any) -> bool:
        return value in _direction_strict
    
    @classmethod
    def __to_py_obj__(cls, value: str, *, verified: bool = False) -> Self:
        value = super().__to_py_obj__(value, verified=verified)
        return cls(direction=value)
    
    def __to_bloks__(self, *args, **kwargs) -> str:
        return self.direction.value
    
class DifferentAlignment(str, Enum):
    start: str = "start"
    center: str = "center"
    end: str = "end"
    stretch: str = "stretch"
    flex_start: str = "flex_start"
_alignment_strict = enum_list(DifferentAlignment)
class Alignment(BlokFieldType):
    alignment: DifferentAlignment

    @classmethod
    def test_for(cls, value: Any) -> bool:
        return value in _alignment_strict
    
    @classmethod
    def __to_py_obj__(cls, value: Any, *, verified: bool = False) -> Self:
        value = super().__to_py_obj__(value, verified=verified)
        return cls(alignment=value)
    
    def __to_bloks__(self, *args, **kwargs) -> str:
        return self.alignment

class DifferentJustify(str, Enum):
    space_evenly: str = "space_evenly"
    flex_start: str = "flex_start"
_justify_strict = enum_list(DifferentJustify)
class Justify(BlokFieldType):
    justify: DifferentJustify

    @classmethod
    def test_for(cls, value: Any) -> bool:
        return value in _justify_strict
    
    @classmethod
    def __to_py_obj__(cls, value: Any, *, verified: bool = False) -> Self:
        value = super().__to_py_obj__(value, verified=verified)
        return cls(justify=value)
    
    def __to_bloks__(self, *args, **kwargs) -> str:
        return self.justify.value

class SizeUnits(str, Enum):
    percentage: str = "%"
    dpi: str = "dp"
_re_dpi_ending_with_dp = re.compile(r"(\d+(\.\d+)?)(dp|%)")
class DisplaySize(BlokFieldType):
    size: int | float = Field(ge=0)
    unity: SizeUnits

    @classmethod
    def test_for(cls, value: Any) -> bool:
        return _re_dpi_ending_with_dp.match(value) if isinstance(value, str) else False

    @classmethod
    def __to_py_obj__(cls, value: str, *, verified: bool = False) -> Self:
        value = super().__to_py_obj__(value, verified=verified)
        match_groups = _re_dpi_ending_with_dp.match(value).groups()
        return cls(size=eval(match_groups[0]), unity=match_groups[-1])
    
    def __to_bloks__(self, *args, **kwargs) -> str:
        return str(self.size) + self.unity

_re_rgb_color = re.compile(r"(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{8})")
class RGB_or_RGBA_Color(BlokFieldType):
    r: int | float = Field(ge=0, le=255)
    g: int | float = Field(ge=0, le=255)
    b: int | float = Field(ge=0, le=255)
    a: int | float = Field(None, ge=0, le=255)

    @classmethod
    def test_for(cls, value: Any) -> bool:
        return _re_rgb_color.match(value) if isinstance(value, str) else False
    
    @classmethod
    def __to_py_obj__(cls, value: Any, *, verified: bool = False) -> Self:
        value = super().__to_py_obj__(value, verified=verified)
        mode = "rgba" if len(value) == 9 else "rgb"
        return cls(**dict(zip(mode, hex_to_rgb(value))))
    
    def __to_bloks__(self, *args, **kwargs) -> dict:
        return rgb_to_hex([item for item in [self.r, self.g, self.b, self.a] if item is not None])

_re_url = re.compile(r"^https?://.+")
class URL(BlokFieldType):
    url: str = Field(regex=_re_url.pattern)

    @classmethod
    def test_for(cls, value: Any) -> bool:
        return _re_url.match(value) if isinstance(value, str) else False

    def __to_bloks__(self, *args, **kwargs) -> str:
        return self.url

class DifferentTextStyle(str, Enum):
    light: str = "light"
    normal: str = "normal"
    medium: str = "medium"
    semibold: str = "semibold"
    bold: str = "bold"
    heavy: str = "heavy"
    italic: str = "italic"
    bold_italic: str = "bold_italic"
_text_style_strict = enum_list(DifferentTextStyle)
class TextStyle(BlokFieldType):
    text_style: DifferentTextStyle = "normal"

    @classmethod
    def test_for(cls, value: str) -> bool:
        return value in _text_style_strict
    
    @classmethod
    def __to_py_obj__(cls, value: Any, *, verified: bool = False) -> Self:
        value = super().__to_py_obj__(value, verified=verified)
        return cls(text_style=value)
    
    def __to_bloks__(self, *args, **kwargs) -> str:
        return self.text_style.value
    
_re_text_size = re.compile(r"\d+(\.\d+)?sp")
class TextSize(BlokFieldType):
    text_size: int | float = Field(ge=0)

    @classmethod
    def test_for(cls, value: str) -> bool:
        return _re_text_size.match(value) if isinstance(value, str) else False

    @classmethod
    def __to_py_obj__(cls, value: str, *, verified: bool = False) -> Self:
        value = super().__to_py_obj__(value, verified=verified)
        return cls(text_size=eval(value.replace("sp", "")))
    
    def __to_bloks__(self, *args, **kwargs) -> str:
        return self.text_size
    
def find_type(*values: Any) -> tuple[type]:
    if all([isinstance(value, str) for value in values]):
        ""