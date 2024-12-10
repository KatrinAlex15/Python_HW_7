
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
     def __init__(self, driver):
         self.driver = driver
         self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


     def set_delay(self, delay):
         delay_input = self.driver.find_element(By.ID, "delay")
         delay_input.clear()
         delay_input.send_keys(delay)


     def click_button(self, button):
         self.driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

     def return_result(self, EC_result):
         wait = WebDriverWait(self.driver, 50)
         result = wait.until(
             EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), EC_result)
         )
         result = self.driver.find_element(By.CSS_SELECTOR, '.screen')
         return result.text
