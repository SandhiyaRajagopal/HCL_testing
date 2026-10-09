
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://assertqa.com/practice/webtables")
driver.maximize_window()

# TC01: Print all column headings
headings = driver.find_elements(By.XPATH, "//table//th")
print("TC01: Column Headings")
for h in headings:
    print(h.text)

# Get all data rows
rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

# TC02: Print first data row
print("TC02: First Row")
print(rows[0].text)

# TC03: Print last data row
print("TC03: Last Row")
print(rows[-1].text)

# TC04: Search employee by last name
name = input("Enter last name: ")
for row in rows:
    if name.lower() in row.text.lower():
        print("TC04: Matching Record:", row.text)

# TC05: Print all email addresses
print("TC05: Email Addresses")
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        if "@" in cell.text:
            print(cell.text)

# TC06: Find employee with highest Due
highest = -1
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        try:
            amount = float(cell.text.replace("$", "").replace(",", ""))
            if amount > highest:
                highest = amount
                employee = row.text
        except ValueError:
            pass

print("TC06: Highest Due Employee:", employee)
print("Highest Amount:", highest)

# TC07: Verify website link
url = "https://assertqa.com/practice/webtables"
if driver.current_url == url:
    print("TC07: PASS")
else:
    print("TC07: FAIL")

# TC08: Count data rows
print("TC08: Total Rows:", len(rows))

input("Press Enter to close browser")
driver.quit()
