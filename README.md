# stepik-python-selenium-project

Hi, there🖐! This is my Automation testing project on Stepik education platform. Course is [here](https://stepik.org/course/575/syllabus)

# Tech stack

python 3.8, pytest, selenium

# Setup

* Ensure you have pipenv available. 
* Ensure you have cloned this repo and are in the project root directory that has the Pipfile with definitions of all required dependencies.
* Execute `pipenv shell` to activate the virtualenv in your terminal
* Execute `pipenv install` to install all dependencies
* Execute `pytest -v --tb=line --language=en test_main_page.py`

# Project structure

* `pages` dir contains application pages base classes, functions, locators
* `conftest.py` has configuration pytest fixtures
* `test_main_page.py` and `test_product_page.py` have tests
