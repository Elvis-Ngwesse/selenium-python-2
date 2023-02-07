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
- cd steps
- pytest

****************************
Run Tests with allure report
****************************
- cd testCases
- cd steps
- pytest --alluredir=reports test_steps_veg_count.py
- allure serve reports