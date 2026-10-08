from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
import os
import time

# Open Chrome
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
# TC01 - Open registration page
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")

driver.maximize_window()

time.sleep(10)

# TC02 - Enter First Name
driver.find_element(
    By.XPATH,
    "//input[@placeholder='First Name']"
).send_keys("Sandhiya")

time.sleep(2)
# TC03 - Enter Email
driver.find_element(
    By.XPATH,
    "//input[@placeholder='name@example.com']"
).send_keys("sandhiya@gmail.com")

time.sleep(2)
# TC04 - Select Gender - Female
# driver.find_element(By.XPATH, "//label[text()='Female']/preceding-sibling::input").click()
driver.find_element(By.XPATH, "(//input[@type='radio'])[2]").click()

time.sleep(2)
# TC05 - Enter Mobile Number
driver.find_element(
    By.XPATH,
    "//input[@placeholder='Enter Mobile Number']"
).send_keys("9876543210")
time.sleep(2)   
# TC06 - Enter Date of Birth
driver.find_element(
    By.XPATH,
    "//input[@type='date']"
).send_keys("15-08-2005")
time.sleep(2)
# TC07 - Enter Subject
driver.find_element(
    By.XPATH,
    "//input[@placeholder='Enter Subject']"
).send_keys("Python")
time.sleep(2)   
# # TC08 - Select Hobbies - Reading
# driver.find_element(
#     By.XPATH,
#     "//input[@value='reading']"
# ).click()

# TC09 - Select Hobbies - Music
driver.find_element(By.XPATH, "//label[normalize-space()='Music']/parent::div/input").click()
time.sleep(2)

picture = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//input[@type='file' and @id='picture']"
        )
    )
)

file_path = r"C:\Users\admin\Downloads\PASSPORT PIC.jpeg"

if os.path.isfile(file_path):

    picture.send_keys(file_path)

    print("Picture selected successfully")

else:

    print("Picture file not found:")
    print(file_path)

time.sleep(3)

address = driver.find_element(
    By.XPATH,
    "//textarea[@id='picture']"
)
address.send_keys("Chennai, Tamil Nadu")
time.sleep(2)
# Select State
state = Select(
    driver.find_element(By.XPATH, "//select[@id='state']")
)

state.select_by_visible_text("NCR")


city = driver.find_element(
    By.XPATH,
    "//select[@id='city']"
)

Select(city).select_by_visible_text("Agra")


# TC13 - Submit
driver.find_element(
    By.XPATH,
    "//input[@type='submit' and @value='Login']"
).click()

time.sleep(3)

# TC14 - Verify successful submission
print("Form submitted successfully")

# Keep browser open
input("Press Enter to close...")

driver.quit()