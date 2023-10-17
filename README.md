# aqa.2023.mr
This  framework is desgned to automate UI and API tests, providing a structured and efficient approach to testing various aspects of a project. 


## Framework structure
### Config module

This module includes configuration settings and parameters essential for the functioning of the testing framework. It allows for centralized management of settings, making it easier to adaptation the testing env and behavior as needed.

How to add:
src/config/config.py

### Application module
The application module is a core components that includes functionality to interact with the application under test.

How to add:
1. API sub-module: scr/applications/api/github_api.py
2. UI sub-module: scr/application/ui/github_ui.py

### Helpers module
This module contains functions and utilities that assist in the testing process.

How to add: src/helpers/helpers.py

### Tests module
 This module contains the actual tests that validate the application's behavior. It's where you write , organize, and execute test scripts, ensuring that the application meets specified requirements and functions correctly in different scenarios.

How to add:
1. API sub-module: tests/github/api/test_api.py
2. UI sub-module: tests/github/ui/test_ui.py
