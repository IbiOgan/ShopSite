import urllib
from urllib.parse import urljoin
from behave import given, when, then


@given(u'we want to view products on the site')
def step_impl(context):
    base_url = f'{context.test_case.live_server_url}/'
    print('base_url:', base_url)
    open_url = urljoin(base_url, '/store/')
    print('open_url:', open_url)
    context.browser.get(open_url)


@when(u'we visit the product page')
def step_impl(context):
    pass


@then(u'Then it loads successfully')
def step_impl(context):
    pass
    # assert context.welcome_page.response.status_code == 200
