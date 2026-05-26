import allure
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

@allure.title("stale_element")
@allure.description("stale_element")
def test_stale_element_exp_demo():
    edge_service = EdgeService()
    driver = webdriver.Edge(service=edge_service)
    driver.get("https://google.com")
    try:
        textarea = driver.find_element(By.NAME, "q")
        # Refresh the page, which invalidates the 'textarea' element
        driver.refresh()
        # This will raise a StaleElementReferenceException
        textarea.send_keys("The Testing Academy")
    except StaleElementReferenceException as see:
        # Catch the exception and print a descriptive message
        print(f"Stale element reference caught: {see}")
    finally:
        driver.quit()
# To run the script, you would typically call the function directly
# or use a test runner like pytest.
# test_stale_element_exp_demo()
