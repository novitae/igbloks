from pydantic.dataclasses import dataclass
from typing import Literal

@dataclass(frozen=True)
class BaseData:
    id: str
    """The id of the variable."""

    type: Literal["gs", "ls"]
    """The type of the variable."""

