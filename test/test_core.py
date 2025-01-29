from igbloks.core import BlokResponse
from pydantic import ValidationError
import pytest

from .content import (
    com__bloks__www__ig__about_this_account__graphql_www,
    com__bloks__www__ig__about_this_account__ios,
    com__bloks__www__ig__about_this_account__web,
)

def test_load_any():
    BlokResponse.from_response(com__bloks__www__ig__about_this_account__graphql_www)
    BlokResponse.from_response(com__bloks__www__ig__about_this_account__ios)
    BlokResponse.from_response(com__bloks__www__ig__about_this_account__web)
    with pytest.raises(ValueError):
        BlokResponse.from_response("hello")

def test_bkid():
    BlokResponse.from_response(com__bloks__www__ig__about_this_account__graphql_www, bkid="16e9197b928710eafdf1e803935ed8c450a1a2e3eb696bff1184df088b900bcf")
    with pytest.raises(ValidationError):
        BlokResponse.from_response(com__bloks__www__ig__about_this_account__graphql_www, bkid="aaa")