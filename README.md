Python Playwright API & UI Automation Project

Test automation project created to demonstrate API testing using Python, Pytest and Allure.

About the Project

The project contains automated tests for REST API functionality.

The main goal is to demonstrate practical skills in:

API test automation
Positive and negative testing
Pytest framework
Test fixtures
Test reporting with Allure
Environment configuration
Git and GitHub
Technologies
Python 3.12
Pytest
Requests
AssertPy
Allure Report
python-dotenv
Git / GitHub
Project Structure
Python_Playwright_API_UI_Project/
?
??? api/
?   ??? user_api.py
?
??? tests/
?   ??? api/
?       ??? test_users_positive.py
?       ??? test_users_negative.py
?
??? .env
??? .gitignore
??? conftest.py
??? pytest.ini
??? requirements.txt
??? README.md
API Testing

The API part of the project uses the GoRest REST API.

Implemented operations:

GET — retrieve users
POST — create a user
PATCH — partially update a user
PUT — update a user
DELETE — delete a user
API Test Coverage

The test suite includes:

Positive tests
Negative tests
User retrieval by ID
User filtering
User creation
User update
User deletion
Full CRUD lifecycle
Test Data and Configuration

Environment-specific data is stored in a .env file.

Sensitive information such as API tokens is not stored in the source code.

The .env file is excluded from Git using .gitignore.

Test Fixtures

Pytest fixtures are used to provide reusable API objects and test setup.

Allure Reporting

The project uses Allure for test reporting.

Tests include Allure metadata such as:

Feature
Story
Test descriptions

To generate Allure results:

pytest tests/api/ --alluredir=allure-results

To open the Allure report:

allure serve allure-results
Running Tests

Install dependencies:

pip install -r requirements.txt

Run all tests:

pytest

Run API tests:

pytest tests/api/

Run positive tests:

pytest -m positive

Run negative tests:

pytest -m negative
Test Results

Allure Report provides detailed information about test execution, including test status, features, stories and test descriptions.

Future Improvements

The project will be extended with UI automation using Playwright.

Planned improvements include:

Page Object Model
UI positive and negative tests
Playwright fixtures
Test parametrization
Screenshots and traces for failed tests
API + UI integration scenarios
Extended Allure reporting
CI/CD integration
Author

Natali Turchyna

QA Engineer | Manual & Automation Testing

Skills demonstrated in this project:

Python · Pytest · REST API · Allure · Git · GitHub