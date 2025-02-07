from pydantic.dataclasses import dataclass
from typing import Literal

@dataclass(frozen=True)
class Size:
    value: float
    type: Literal["dp", "%", "px"]