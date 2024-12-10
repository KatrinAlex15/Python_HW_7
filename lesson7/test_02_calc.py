import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()
def test_02_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.set_delay("45")
    calculator_page.click_button("7")
    calculator_page.click_button("+")
    calculator_page.click_button("8")
    calculator_page.click_button("=")

    assert calculator_page.return_result("15") == "15"

    driver.quit()