import pytest

from tests.base_url_test import BASE_URL
from utils.validation_utils import *

FACTS_ENDPOINT = f"{BASE_URL}/facts"

@pytest.mark.must_pass
def test_facts_endpoint_valid_status_code():
    assert_valid_status_code("get", FACTS_ENDPOINT, 200)


def test_facts_endpoint_valid_content_type():
    assert_valid_content_type(FACTS_ENDPOINT, "application/json; charset=UTF-8")


def test_facts_endpoint_invalid_content_type():
    assert_invalid_content_type(FACTS_ENDPOINT, "text/html; charset=UTF-8")


def test_facts_endpoint_invalid_status_code():
    assert_invalid_status_code("post", FACTS_ENDPOINT, 200)
    assert_invalid_status_code("update", FACTS_ENDPOINT, 200)
    assert_invalid_status_code("delete", FACTS_ENDPOINT, 200)


def test_facts_endpoint_response_has_multiple_results():
    response = requests.get(f"{FACTS_ENDPOINT}/random")
    data     = response.json()
    assert len(data) > 0 , f"Endpoint /facts did not returned 0 objects."


def test_facts_random_endpoint_is_not_empty():
    response = requests.get(f"{FACTS_ENDPOINT}/random")
    assert response.text != "", "Endpoint 'facts/random returned an empty object."
    data = response.json()
    assert data['_id'] != "" , "Endpoint /facts/random returned 0 objects."


@pytest.mark.parametrize("animal_type,amount", [("cat", 2), ("cat",100)])
def test_facts_random_endpoint_returns_valid_animal_type_and_amount(animal_type, amount):
    query    = f"?animal_type={animal_type}&amount={amount}"
    response = requests.get(f"{FACTS_ENDPOINT}/random{query}")
    data     = response.json()
    for o in data:
        for attr, value in o.items():
            if attr == "type":
                assert value == animal_type, \
            f"Returned JSON includes an object with an invalid animal_type. Expected {animal_type} found {value}. Object: {o}"
    assert len(data) == amount , f"Query {query} returned invalid amount. Expected {amount} found {len(data)}."


@pytest.mark.parametrize("animal_type", ["truck"])
def test_facts_random_endpoint_returns_empty_with_invalid_animal_type(animal_type):
    query    = f"?animal_type={animal_type}"
    response = requests.get(f"{FACTS_ENDPOINT}/random{query}")
    assert response.text == "", f"Query {query} JSON response is not empty.Expected {0} found {response.text}."
