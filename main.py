from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

DRIVER_PATH = 'C:/Users/seema/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://finance.yahoo.com/quote/AAPL/community?p=AAPL')
h2 = 'o'

# Goes to new comments in Yahoo Finance
def new_comments():
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div/div/div/div[2]/button"))
        )


    finally:
        h1 = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div/div/div/div[2]/button")
        h1.click()


def get_replies():
    list_elements = driver.find_elements(By.XPATH, ("//button[contains(@class, 'replies-button')]"));

    for items in list_elements:
        items.click()

def get_comments():
    list_elements = driver.find_elements(By.XPATH, ("//div[contains(@class, 'C($c-fuji-grey-l)')]"));
    for items in list_elements:
        print(items.text)


try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,
            "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div/div/div/div[2]/ul/li[2]/button"))
        )

finally:
       h2 = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div/div/div/div[2]/ul/li[2]/button")


h2.click()
time.sleep(1)

get_replies()



get_comments()

driver.quit()
