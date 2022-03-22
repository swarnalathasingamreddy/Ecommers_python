from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:\\Webdriver\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com/.com")

# Selenium with python:
# ->How to fimd how many input boxes present in webpage
# for this we need to identify the common attribue which is having the every test box
Input_boxes = driver.find_elements(By.CLASS_NAME "text_field")
print(len(Input_boxes))
#
# -->How to provide value into texebox>
driver.find_element(By.ID,"Text_Filed")
#
#
# -->To verify that Radio button is selected or not by using isselected()

status = driver.find_element_by_id("Tesulu_Rado").is_enabled()

print(status)   #if it is selected status will show True else false

driver.find_element_by_id("Tesulu_Rado").click()

# For dropdown we should use select class
select by text
selct by index
select by value

# links

# for all links there should be anchor tag is there ...that ia call a (a is the tag name)
links = driver.find_elements(By.TAG_NAME,"a")

print(len(links))  # here it will display all the linsks in the same page.

suppose i want to read all the lnks from link variable

for link in links:
    print(link.text)

to findout and captureture all links we have 2 approches (linktext and parcel linktext )

for link text we should give entire link of the text
for partial link text we should give substring of the link text

# Alert windows
    driver.switch_to_alert().accept() -->it will accept ok button
driver.switch_to_alert().dismiss() -->it will click on cancel button

#working with browser windoes
driver.current_window_handle
driver.window_handles

