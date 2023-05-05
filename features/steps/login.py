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
