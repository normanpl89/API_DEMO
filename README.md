## Getting Started

This is the quick and easy getting started assuming you already have git and pip installed.

```sh
# Install the required items
1. Remove your current version of virtualenv (optional)
pip uninstall virtualenv

2. Install pipenv
pip install --user pipenv

3. Testing the installation
pipenv --version

4. Install dependencies
pipenv install Pipfile 

5. Switch to pipenv virtual environment
pipenv shell

6. Run tests 
# To run all the test scenarios:
pytest

# to run scenarios with specific tags:
pytest -m get_fact_result_invalid_id
```


## Pytest - Test Runner
Method with test_ or _test will be collected, Pytest support several way to run test:
- Run test with method: ```pytest test_class.py```
- Run tests in a package: ```pytest testing/```
- Run tests by marker expressions: ```pytest -m slow``` (custom marker defined by this line of code ```@pytest.mark.<custom_marker_name>```)
