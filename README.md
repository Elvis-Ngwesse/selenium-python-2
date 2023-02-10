# Selenium-Python
Selenium Python framework

**********************
Installing virtual env 
**********************
- pip install virtualenv
- virtualenv venv
- source venv/bin/activate


**********************
Install requirements.txt
**********************
- pip3 install -r requirements.txt
- pip3 freeze > requirements.txt

**********************
Run Tests
**********************
- cd testCases
- cd tests
- pytest

****************************
Run Tests with allure report
****************************
- cd testCases
- cd tests
- pytest --alluredir=reports test_deals.py
- allure serve reports