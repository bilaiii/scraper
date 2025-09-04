from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException, ElementNotInteractableException
from getpass import getpass
from time import sleep
from dotenv import load_dotenv
from os import getenv

options = webdriver.FirefoxOptions()
# options.add_argument("-headless")
driver = webdriver.Firefox(options=options)

ignore = [NoSuchElementException, ElementNotInteractableException]
wait = WebDriverWait(driver, timeout=100, poll_frequency=.2, ignored_exceptions=ignore)

load_dotenv()

def main():
    str: login 
    str: passwd 

    login = getenv("LOGIN")
    passwd = getenv("PASSWD")
    driver.get("https://vilni-zl.edus.school/login")

    wait.until(lambda _ : driver.find_elements(By.TAG_NAME, "input"))
    
    # sleep(1)

    # login = input("Your login: ")
    # passwd = getpass("Your password: ")
    
    inputs = driver.find_elements(By.TAG_NAME, "input")

    inputs[0].send_keys(login)
    inputs[1].send_keys(passwd)

    driver.find_element(By.XPATH, "//button[@class='blue']").click()

    wait.until(lambda _ : "Головна" in driver.title)

    print("""What do you want to do?
            1. See a list of homework tasks
            2. See my notifications""")
    inp = input("Choose here: ")
    if "1" in inp:
        driver.get("https://vilni-zl.edus.school/pupils/tasks")
        wait.until(lambda _ : driver.find_elements(By.CLASS_NAME, "future"))
        tasks = driver.find_elements(By.CLASS_NAME, "future")
        compareDate = ""
        for e in tasks:
            title = e.find_element(By.XPATH, ".//p[@class='title']")
            body = e.find_element(By.XPATH, ".//div[@class='task']")
            date = e.find_element(By.XPATH, ".//p[@class='prepare-till']/span")
            if date.text != compareDate:
                print("## " + date.text + "\n")
            compareDate = date.text
            print("- [ ] " + title.text, "\n" + body.text[12:], "\n")
    elif "2" in inp:
        driver.get("https://vilni-zl.edus.school/pupils/notifications")
        wait.until(lambda _ : driver.find_elements(By.CLASS_NAME, "notifications-wrap"))
        notifications = driver.find_elements(By.CSS_SELECTOR, ".notifications-wrap.is-new")
        print(notifications)
                
    driver.quit()
if __name__ == '__main__':
    main()
    
