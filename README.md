# Pytest

# HOW TO CONFIGURE AND USE DJANGO PYTEST?

# after makeing project and app:
# 1- make tests folder 
# 2- install pytest -> pip install pytest-django
# 3- make pytest.ini file and add these on ->
#    -- FILE: pytest.ini (or tox.ini)
#   [pytest]
#   DJANGO_SETTINGS_MODULE = test.settings
#   -- recommended but optional:
#   python_files = tests.py test_*.py *_tests.py

# 4- write your tests
# 5- for running:
# - pytest                                 # run all tests
# - pytest a_directory                     # directory
# - pytest test_something.py               # tests file
# - pytest test_something.py::single_test  # single test function

<!-- *************************************************************** -->

# a pattern for writing tests
# 1- Arrange:
# - prepare any state you need to perform the action you want to try.
# - trying to prepare and ready test to perform the action at the second stage the act.
# + does the test require any objects? or sepecially settings? 
# + does it need any DB at all to run the test? 
# + do we need to login in any web, app? 
# + do we need to connect to any API?

# 2- Act:
# - we're performing an action.
# - this could calling a functional method or maybe calling a REST-API or inteacting with a web page.
# - typically this step should listen to some sort of response
# + this step should have some sort of response 
# + hhtp response or data which return from an API

# 3- Assert
# - assert expected outcomes
# - take the response from the act step and test it agenst the expected outcome of performing the action
# - if we were mean to return some data from act step then the assert is going to test to see if that data was indeed returned.
# - if we do assert the action or the act and we have return the expected outcome then return True.

# pytest fixtuers:
# - are functions
# - run before/after each test function to which the fixture is applied.
# + we use fixtures to collect data from DB or for prepare a DB connection so then we can perform a function in the act to return response and then we can assert the response to check to see if we return an expected outcome.
# + fixtures are used to feed data to the tests such as DB connections, URLs to test and input data.



