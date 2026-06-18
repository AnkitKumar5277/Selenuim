# Import necessary libraries
import time
import allure 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

@allure.title("Opencart Registration Account Testing With Selenium_Mini_Project 3")
@allure.description("TC1 - Positive TC - Fill the registration form with valid data and verify account creation")
@pytest.mark.positive

# Set up the Edge browser in private mode
options = webdriver.EdgeOptions()
options.add_argument("--inprivate")  # Opens browser in private mode
driver = webdriver.Edge(options=options)  # Start the Edge browser
driver.maximize_window()  # Make the browser window full-screen

# Step 1: Open the website
driver.get("https://katalon-demo-cura.herokuapp.com/")  # Visit the CURA Healthcare website

# Step 2: Click the "Make Appointment" button
# Wait up to 10 seconds for the button to be clickable
appointment_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "btn-make-appointment"))
)
appointment_button.click()  # Click the button

# Step 3: Log in to the website
# Wait for the login fields to appear
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txt-username")))
# Enter username and password
driver.find_element(By.ID, "txt-username").send_keys("John Doe")
driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
# Click the login button
driver.find_element(By.ID, "btn-login").click()

# Step 4: Fill out the appointment form
# Wait for the form to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "combo_facility")))
time.sleep(1)  # Short pause to ensure stability

# Select "Hongkong CURA Healthcare Center" from the dropdown
facility_dropdown = Select(driver.find_element(By.ID, "combo_facility"))
facility_dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")
time.sleep(1)  # Short pause

# Check the "Apply for hospital readmission" checkbox
driver.find_element(By.ID, "chk_hospotal_readmission").click()
time.sleep(1)  # Short pause

# Select the "Medicaid" radio button
driver.find_element(By.CSS_SELECTOR, "input[value='Medicaid']").click()
time.sleep(1)  # Short pause

# Step 5: Select a date
# Click the date input field
date_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "txt_visit_date"))
)
date_input.click()
time.sleep(1)  # Short pause

# Select the day "30" from the calendar
date_to_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//td[text()='30']"))
)
date_to_select.click()
time.sleep(1)  # Short pause

# Step 6: Add a comment
# Find the comment box, clear it, and type a message
comment_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "txt_comment"))
)
comment_box.clear()  # Clear any existing text
comment_box.send_keys("This is an automated appointment request.")
time.sleep(1)  # Short pause

# Step 7: Book the appointment
driver.find_element(By.ID, "btn-book-appointment").click()
time.sleep(1)  # Short pause

# Print a success message
print("Appointment successfully booked! Browser will close in 10 seconds.")

# Wait for 10 seconds before closing
time.sleep(10)

# Close the browser

driver.quit()

# pytest -s main.py --alluredir=reports
# allure serve reports
