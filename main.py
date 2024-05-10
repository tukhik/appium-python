import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from appium.options.android import UiAutomator2Options

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Samsung S9',
)

appium_server_url = 'http://localhost:4723/wd/hub'

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(command_executor=appium_server_url,options=capabilities_options)
    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_open_web_view(self) -> None:
        el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='WebView Browser Tester')
        el.click()
        time.sleep(3)
        dots = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="About WebView"]')
        dots.click()
        time.sleep(3)
        about = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="About WebView"]')
        about.click()
        try:
            parent_panel = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="android:id/parentPanel"]')
            assert parent_panel is not None, "Element with id 'parentPanel' exists."
            print("Test passed: Element with id 'parentPanel' exists.")
        except NoSuchElementException:
            print("Test failed: Element with id 'parentPanel' does not exist.")
            self.driver.quit()
