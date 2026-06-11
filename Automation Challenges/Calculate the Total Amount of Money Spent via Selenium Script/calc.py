import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
 
# This function will run the test in the given browser
def run_test(browser_name):
    # 1. Open the browser
    if browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "chrome":
        driver = webdriver.Chrome()
    else:
        print("❌ Browser not supported")
        return

    driver.maximize_window()
    driver.get("https://demo.applitools.com")  # open demo site

    # 2. Login into the site
    time.sleep(2)  # wait for page to load
    driver.find_element(By.ID, "username").send_keys("Admin")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("Password@123")
    time.sleep(1)
    driver.find_element(By.ID, "log-in").click()
    time.sleep(2)

    # 3. Get all amount values from the table
    rows = driver.find_elements(
        By.XPATH,
        "//table[@class='table table-padded']//td[@class='text-right bolder nowrap']/span"
    )

    numbers = []
    for row in rows:
        value = row.text.strip()  # Example: "+ 1,250 USD"
        if value:
            # Clean text → remove symbols like + , $ , USD , spaces
            value = value.replace("+", "").replace("$", "").replace(",", "").replace("USD", "").strip()
            value = value.replace(" ", "")  # change "- 320" → "-320"
            try:
                numbers.append(float(value))  # convert to number
            except:
                print("⚠️ Skipped invalid value:", value)

    # 4. Add all numbers
    total_sum = sum(numbers)

    # Print results
    print(f"\n🌐 Browser: {browser_name.upper()}")
    print("Extracted values:", numbers)
    print("✅ Total Sum =", total_sum)

    time.sleep(3)  # just to see result in browser
    driver.quit()
    print(f"🚀 Test finished in {browser_name.upper()}")


# Run test in both browsers at the same time
t1 = threading.Thread(target=run_test, args=("edge",))
t2 = threading.Thread(target=run_test, args=("chrome",))

t1.start()
t2.start()

t1.join()
t2.join()

print("\n🎉 Both browsers completed successfully!")
