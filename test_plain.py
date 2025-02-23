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
        page.goto("https://www.levi.com/US/en_US/")
    with allure.step("Assert"):
        assert page.title() == "Jeans, Denim Jackets &amp; Clothing | Levi&#x27;s® Official Site"

    with allure.step("Capture Screenshot"):
        screenshot_path = "allure_results/practice-test-login.png"
        page.screenshot(path=screenshot_path)
        
        # Attach screenshot to Allure
        with open(screenshot_path, "rb") as image:
            allure.attach(image.read(), name="login_screenshot", attachment_type=allure.attachment_type.PNG)
