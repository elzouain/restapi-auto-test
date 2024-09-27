# REST API Automation Example

A Python project to perform several API tests against the [Cat Facts API](<https://alexwohlbruck.github.io/cat-facts/>).

# Test Approach 

This project will perform <b>Validation Testing</b> to ensure the content received is the expected, as 
detailed in the [Cat Facts API documentation page.](<https://alexwohlbruck.github.io/cat-facts/docs/endpoints/facts.html/>)


# Test Cases

<b>BASE URL:</b> https://cat-fact.herokuapp.com

| Endpoint      | Parameters  | Values  | Expected Result                                 |
|---------------|-------------|---------|-------------------------------------------------| 
| BASE URL      | --          | --      | Content type is <i>text/html; charset=UTF-8</i> |
| /facts        | --          | --      | Content type is <i>application/json; charset=UTF-8</i>         |
| /facts        | --          | --      | Response with multiple unsorted objects.        |
| /facts/random | --          | --      | Returns a single random object.                 |
| /facts/random | animal_type | 'cat'   | Returns an object with 'type' equals 'cat'      |
| /facts/random | animal_type | 'truck' | Empty response.                                 |
| /facts/random | amount      | n       | Matching amount of n results.                   |

# Requirements

* Python 3.10.12
* pip 23.2.1
* pytest 8.3.3
* requests 2.32.3
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>) (recommended)
* Full list of dependencies in `requirements.txt`

# Installation

1. Clone the repository `git clone https://github.com/elzouain/restapi-auto-test.git`
2. Change to this project's root directory `cd restapi-auto-test`
3. Run `python3 -m venv .venv` to create the `./.venv/` directory.
If you get an error, use `sudo apt install python3.10-venv` and try again.
4. Change the executable permissions of the virtual environment activation script `sudo chmod 777 ./.venv/bin/activate`
5. Activate the virtual environment `source ./.venv/bin/activate` (UNIX systems). 
You should see `(.venv)` next to the terminal prompt.
6. Within the virtual environment, install the necessary dependencies `pip install -r requirements.txt`
7. To exit the virtual environment run `deactivate`.

# Test Execution

1. Open a terminal
2. From the project root directory run `pytest -v --html=results/report.html`
