import string

import requests
from requests import request


def assert_valid_status_code(request_type: string, url: string, expected_status_code=200):
    response = request(request_type, url)
    assert response.status_code == expected_status_code, \
        f"Incorrect status code. Expected {expected_status_code} found {response.status_code}."

def assert_invalid_status_code(request_type: string, url: string, invalid_status_code):
    response = request(request_type, url)
    assert response.status_code != invalid_status_code, \
        f"Invalid status code received. Not expected {invalid_status_code} found {response.status_code}."

def assert_valid_content_type(url: string, content_type: string):
    response = requests.get(url)
    found    = response.headers['Content-Type']
    assert found.casefold() == content_type.casefold(), \
        f"Incorrect Content-Type. Expected {content_type} found {found}."

def assert_invalid_content_type(url: string, invalid_content_type: string):
    response = requests.get(url)
    found    = response.headers['Content-Type']
    assert found.casefold() != invalid_content_type.casefold(), \
        f"Incorrect Content-Type received. Expected {invalid_content_type} found {found}."
