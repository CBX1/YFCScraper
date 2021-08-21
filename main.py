from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time



def initialize(string):
    string = string.capitalize()
    DRIVER_PATH = 'C:/Users/seema/Downloads/chromedriver'
    options = webdriver.ChromeOptions();
    # options.add_argument('headless');
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
    driver.get('https://finance.yahoo.com/quote/' + string + '/community?p=' + string)
    return driver

def show_more(driver,limit=0):
    if limit == 0:
        return
    else:
        try:
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//button[contains(@class, 'Bdrs(4px)')]"))
            )

        finally:
            h2 = driver.find_element_by_xpath(
                "//button[contains(@class, 'Bdrs(4px)')]")
            time.sleep(1)
            h2.click()

            show_more(limit-1)



# Goes to new comments in Yahoo Finance
def string_comment(type):
    string = ""
    if type == "top":
        string = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div/div/div/div[2]/ul/li[1]/button"
    elif type == "new":
        string = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div/div/div/div[2]/ul/li[2]/button"
    elif type == "recent":
        string = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div/div/div/div[3]/ul/li[3]/button"
    elif type == "disc":
        string = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div/div/div/div[3]/ul/li[4]/button"
    elif type == "old":
        string = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div/div/div/div[3]/ul/li[5]/button"
    return string

def new_comments(driver,type):
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div/div/div/div[2]/button"))
        )
    finally:
        h1 = driver.find_element_by_xpath(

            "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div/div/div/div[2]/button")
        h1.click()
    string = string_comment(type)

    try:
        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.XPATH,
                string))
            )

    finally:
           h2 = driver.find_element_by_xpath(
           string)
           h2.click()
           time.sleep(1)




def get_replies(driver):

    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    list_elements = driver.find_elements(By.XPATH, ("//button[contains(@class, 'replies-button')]"));
    time.sleep(1)
    for items in list_elements:
        items.click()

def get_comments(driver,limit=0):
    list_comments = []
    list_elements = driver.find_elements(By.XPATH, ("//div[contains(@class, 'C($c-fuji-grey-l)')]"));
    if limit > 0:
        list_elements= list_elements[:limit]
    for items in list_elements:
            list_comments.append(items.text)
    return list_comments

#checks if comments are available

# driver = initialize('aapl')
# new_comments(driver,'disc')
# show_more(driver,3)
# get_replies(driver)
# a = get_comments(driver)
# print(a)
#
# driver.quit()
