from behave import fixture, use_fixture
import os
os.environ["DJANGO_SETTINGS_MODULE"] = "ShopSite.settings"
import urllib
import django
django.setup()
from django.shortcuts import resolve_url
from django.test import selenium
from django.test.testcases import TestCase
from django.test.runner import DiscoverRunner
from django.test.testcases import LiveServerTestCase
from django.contrib.auth.models import User
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ShopApp.models import *
# from django.contrib.auth.models import User



# Use the chrome driver specific to your version of Chrome browser and put it in ./driver directory
# the driver needs to have the full file path, so use one of these options to pass full path to driver
# CHROME_DRIVER = os.path.join(os.path.join(os.path.dirname(__file__), 'driver'), 'chromedriver')
current_dir = os.path.dirname(os.path.realpath(__file__))
CHROME_DRIVER = os.path.join(current_dir, 'driver/chromedriver')
chrome_options = Options()
# comment out the line below if you want to see the browser launch for tests
# possibly add time.sleep() if required
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")

# add our browser to the context object so that it can be used in all steps


def before_all(context):
    use_fixture(django_test_runner, context)
    browser = webdriver.Chrome(
        options=chrome_options, executable_path=CHROME_DRIVER)
    browser.set_page_load_timeout(time_to_wait=300)
    context.browser = browser


def before_scenario(context, scenario):
    context.test = TestCase()
    context.test.setUpClass()
    use_fixture(django_test_case, context)


def after_scenario(context, scenario):
    context.test.tearDownClass()
    del context.test


def after_all(context):
    context.browser.quit()


@fixture
def django_test_runner(context):
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()
    yield
    context.test_runner.teardown_databases(context.old_db_config)
    context.test_runner.teardown_test_environment()


@fixture
def django_test_case(context):
    context.test_case = LiveServerTestCase
    context.test_case.setUpClass()
    context.user1 = User.objects.create_user(username="dave", password='dave')
    context.user1.is_active = True
    context.user1.save()
    context.product1 = Product.objects.create(
                        product_id="1",
                        category="Smartphone",
                        brand="Apple",
                        price=1000.09,
                        product_name="iPhone 11",
                    )
    context.product1.save()
    context.product2 = Product.objects.create(
                        product_id="1",
                        category="Smartphone",
                        brand="samsung",
                        price=1000.09,
                        product_name="Galaxy 11",
                    )
    context.product2.save()
    yield
    context.test_case.tearDownClass()
    del context.test_case
