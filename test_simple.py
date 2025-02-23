import pytest
import allure
from playwright.sync_api import Page

@allure.epic("Simple UI Testing")
@allure.feature("Example Page")
@allure.story("Example Page Story")
def test_basic_navigation(page: Page):

    allure.dynamic.tag("Smoke")
    allure.dynamic.severity(allure.severity_level.CRITICAL)

    # Navigate to a website
    with allure.step("Open Page"):
      page.goto('https://example.com')
    
    # Simple assertion
    with allure.step("Assert"):
      assert page.title() == 'Example Domain'
    
    # Take a screenshot for Allure report
    page.screenshot(path='example.png')

def test_simple_assertion():
    # A simple test to verify pytest is working
    assert True