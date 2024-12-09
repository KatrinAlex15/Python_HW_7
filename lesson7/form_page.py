from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill_parameters(self, parameter, value):
        self.driver.find_element(By.NAME, parameter).send_keys(value)

    def submit_form(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    def return_result(self, field_name):
        return self.driver.find_element(By.CSS_SELECTOR, f"[id='{field_name}']").value_of_css_property("background-color")
