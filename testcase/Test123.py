from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
driver = webdriver.chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(executable_path="C:\\Users\\gsusw\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")


driver.get("https://youtube.com")
driver.find_element_by_id("passive_signin").click()
driver.find_element_by_id("search").send_keys("Swarna Reddy volgs")
driver.find_element_by_id("search-icon-legacy").click()