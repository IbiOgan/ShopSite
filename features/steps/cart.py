import urllib
from urllib.parse import urljoin
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path


@given(u'Go to the index page')
def step_impl(context):
    """ 
    Navigate to the index page
    """
    context.base_url = f'{context.test_case.live_server_url}/'
    context.browser.get(context.base_url)


@when(u'Click on the cart link')
def step_impl(context):
    """ 
    Find the desired link and click on it
    """
    xpath = "//body/nav[1]/div[1]/div[1]/div[1]/div[1]/a[1]"
    status = context.browser.find_element(
        By.XPATH, xpath).is_displayed()
    # print(status)
    assert status == True
    context.browser.find_element(
        By.XPATH, xpath).click()


@then(u'Then it loads')
def step_impl(context):
    """ 
    if successful, then we should be directed to the store page
    """
    assert context.browser.current_url == f'{context.base_url}cart/'
    assert 'Cart' in context.browser.page_source
    # assert context.welcome_page.response.status_code == 200


@given(u'Go to the store page')
def step_impl(context):
    """ 
    Navigate to the store page
    """
    context.base_url = f'{context.test_case.live_server_url}/store/'
    context.browser.get(context.base_url)


@when(u'Click on add to cart button')
def step_impl(context):
    """ 
    Find the add to cart button and click on it
    """
    xpath = "//body/div[1]/div[1]/div[1]/div[1]/button[1]"
    context.browser.find_element(
        By.XPATH, xpath).click()


@then(u'add one item to cart')
def step_impl(context):
    """
    confirm item in cart is 1
    """
    assert '1' in context.browser.page_source
