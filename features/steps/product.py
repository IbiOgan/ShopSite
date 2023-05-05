import urllib
from urllib.parse import urljoin
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path


@given(u'Navigate to the index page')
def step_impl(context):
    """ 
    Navigate to the index page
    """
    context.base_url = f'{context.test_case.live_server_url}/'
    context.browser.get(context.base_url)


@when(u'Click on the products link')
def step_impl(context):
    """ 
    Find the desired link and click on it
    """
    xpath = "//a[@id='storePages']"
    status = context.browser.find_element(
        By.XPATH, xpath).is_displayed()
    # print(status)
    assert status == True
    context.browser.find_element(By.ID, "storePage").click()


@then(u'Then it loads successfully')
def step_impl(context):
    """ 
    if successful, then we should be directed to the store page
    """
    assert context.browser.current_url == f'{context.base_url}store/'
    assert 'Store' in context.browser.page_source
    # assert context.welcome_page.response.status_code == 200
