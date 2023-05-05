# My Render URL
https://kzelectronics.onrender.com/
# My Data Source(Electronics Store Data) 
https://www.kaggle.com/datasets/mkechinov/ecommerce-purchase-history-from-electronics-store
# Introduction
The project is developed to apply my knowledge of Django Python framework in building a web application. This application is built on open source data from Kaggle.com. The application built with models/tables products, customer(User), order, orderItem and shippingAddress.
# Web App Development
Here are some snippets of code I used while setting up this virtual environment.

  ```python
  cd ShopSite/
  pyenv install 3.11.3
  pyenv local 3.11.3
  python3 -m venv .venv
  source .venv/bin/activate
  pip install --upgrade pip
  pip install django
  pip install -r requirements.txt
  ```
Running of App. Here are some snippets of code I used while setting up this flask application.

  ```python
  python3 manage.py runserver
  ```

Here are some snippets of code I used while setting up the GitHub repo.

  ```python
  git init
  git add README.md
  git commit -m "first commit"
  git branch -M main
  git remote add origin <git url>
  git push -u origin main
  ```

I also choose to use GitHub for version control and code maintenance. From my experience using GitHub, I got more familiar with running commands in the terminal. I also felt less anxiety about my work being lost because it was stored in a remote repository online.  Over time I built the habit of committing and pushing my code to the repository frequently. Using GitHub gave me confidence to experiment with my codebase because I could easily restore a previous save point from the git repository. I learnt to use “branch” command to create another branch where I could attempt to implement different HTML and python features. I will definitely be using git for all my projects in the future.
Here are some snippets of code I used while using the GitHub branch.

  ```python
  git branch
  git checkout -b experiment-with-html-tables
  git push --set-upstream origin experiment-with-html-tables
  git checkout main
  git merge experiment-with-html-tables
  ```

# Maintenance/Testing
Create features folder. Create driver folder and download chrome driver. Create features file. Sample code below.
Create product.feature:

  ```python
  Feature: checking login functionality

    Scenario: view products
        Given Go to the login page
        When I Enter username "dave" and password "dave"
        And Click on login button
        Then user successfully logged in
        
     import urllib
from urllib.parse import urljoin
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path


@given(u'Go to the login page')
def step_impl(context):
    """ 
    Navigate to the login page
    """
    context.base_url = f'{context.test_case.live_server_url}/'
    context.browser.get(context.base_url)


@when(u'I Enter username "{user}" and password "{password}"')
def step_impl(context, user, password):
    """ 
    Find the desired fields and enter the values
    """
    context.browser.find_element(By.ID, "username").send_keys(user)
    context.browser.find_element(By.ID, "password").send_keys(password)


@when(u'Click on login button')
def step_impl(context):
    """ 
    Find the login button and click on it
    """
    xpath = "//button[contains(text(),'Sign in')]"
    context.browser.find_element(
        By.XPATH, xpath).click()


@then(u'user successfully logged in')
def step_impl(context):
    """ 
    the user should be logged in and redirected to the store page
    """
    assert 'Profile' in context.browser.page_source
    assert context.browser.current_url == f'{context.base_url}store/'

  ```
run behave command in terminal to do testing.
