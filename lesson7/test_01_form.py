import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from form_page import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_01_form(driver):
    page = FormPage(driver)
    page.fill_parameters("first-name","Иван")
    page.fill_parameters("last-name","Петров")
    page.fill_parameters("address","Ленина, 55-3")
    page.fill_parameters("e-mail","test@skypro.com")
    page.fill_parameters("phone","+7985899998787")
    page.fill_parameters("city","Москва")
    page.fill_parameters("country","Россия")
    page.fill_parameters("job-position","QA")
    page.fill_parameters("company","SkyPro")

    page.submit_form()
    alert_success_color = "rgba(209, 231, 221, 1)"
    alert_danger_color = "rgba(248, 215, 218, 1)"
    assert page.return_result("first-name")== alert_success_color
    assert page.return_result("last-name") == alert_success_color
    assert page.return_result("address") == alert_success_color
    assert page.return_result("e-mail") == alert_success_color
    assert page.return_result("phone") == alert_success_color
    assert page.return_result("city") == alert_success_color
    assert page.return_result("country") == alert_success_color
    assert page.return_result("job-position") == alert_success_color
    assert page.return_result("company") == alert_success_color
    assert page.return_result("zip-code") == alert_danger_color