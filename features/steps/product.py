import urllib
from urllib.parse import urljoin
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path

# base_dir = Path(__file__).resolve().parent.parent
# driver_dir = Path(base_dir, 'driver/chromedriver')
# driver_dir = str(base_dir) + '/driver/chromedriver.exe'
# str(base_dir) + '/ShopApp/data/kzElectronicStore.csv'


@given(u'Navigate to the index page')
def step_impl(context):
    """ 
    Navigate to the index page
    """
    # context.driver = webdriver.Chrome(driver_dir)
    # base_url = str(context.test_case.live_server_url)+'/'
    # print('base_url:', base_url)
    # context.driver.get(base_url)
    # base_url = f'{context.test_case.live_server_url}'
    # base_url = urllib.request.url2pathname(context.test_case.live_server_url)
    # context.browser.get(base_url)
    context.browser.get('http://localhost:5000')


@when(u'Click on the products link')
def step_impl(context):
    """ 
    Find the desired link and click on it
    """
    pass
    # base_url = f'{context.test_case.live_server_url}/store/'
    # context.browser.get(base_url)
    # status = context.browser.find_element(By.ID, "storePage").is_displayed()
    # print(status)
    # assert status == True


@then(u'Then it loads successfully')
def step_impl(context):
    """ 
    if successful, then we should be directed to the product page
    """
    pass
    # status = context.browser.find_element(By.ID, "store_Page").is_displayed()
    # print(context.browser.page_source)
    # assert status == True
    # assert context.browser.current_url == f'{context.test_case.live_server_url}/product/'

# @given(u'we want to view products on the site')
# def step_impl(context):
#     base_url = f'{context.test_case.live_server_url}/'
#     print('base_url:', base_url)
#     open_url = urljoin(base_url, '/store/')
#     print('open_url:', open_url)
#     context.browser.get(base_url)


# @when(u'we visit the product page')
# def step_impl(context):
#     status = context.browser.find_element(By.ID, "store_Page").is_displayed()
#     assert status == True


# @then(u'Then it loads successfully')
# def step_impl(context):
#     pass
#     # assert context.welcome_page.response.status_code == 200
