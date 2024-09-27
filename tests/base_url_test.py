import pytest

from utils.validation_utils import *

BASE_URL = "https://cat-fact.herokuapp.com"

@pytest.mark.must_pass
def test_base_url_valid_status_code():
    assert_valid_status_code("get", BASE_URL, 200)


def test_base_url_valid_content_type():
    assert_valid_content_type(BASE_URL, "text/html; charset=UTF-8")


def test_base_url_invalid_content_type():
    assert_invalid_content_type(BASE_URL, "application/json; charset=UTF-8")


def test_base_url_invalid_status_code():
    assert_invalid_status_code("post", BASE_URL, 200)
    assert_invalid_status_code("update", BASE_URL, 200)
    assert_invalid_status_code("delete", BASE_URL, 200)