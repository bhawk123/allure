import pytest
import allure
from playwright.sync_api import Page

@allure.epic("UI Testing")
@allure.feature("Login Page")
@allure.story("Successful Login")
@pytest.mark.parametrize("username, password", [("student", "Password123")])
def test_login(page: Page, username, password):
    allure.dynamic.tag("Smoke")
    allure.dynamic.severity(allure.severity_level.CRITICAL)

    with allure.step("Open Login Page"):
        page.goto("https://practicetestautomation.com/practice-test-login/")

    with allure.step("Assert"):
        assert page.title() == "Test Login | Practice Test Automation"

    page.screenshot(path='practice-test-login.png')