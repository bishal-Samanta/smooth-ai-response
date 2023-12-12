from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from fp.fp import FreeProxy



def scrape_data_from_bard():
    # Change the URL to the desired website
    url = "https://bard.google.com/chat"

    # Set up the proxy
    proxy = FreeProxy().get()


    # Set up the Chrome options with the proxy
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=%s' % proxy)

    # Open a Chrome browser with the proxy
    driver = webdriver.Chrome(options=options)

    # Open the website
    driver.get(url)


    # Wait for the button to be clickable using aria-label
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Sign in"]'))
    )

    # Click the button
    login_button.click()

    # wait for 2 seconds
    driver.implicitly_wait(2)

    # Find the input tag by its ID
    email_input = driver.find_element(By.ID, "identifierId")

    # Clear the existing value (if any)
    email_input.clear()

    # Enter the email id
    email_input.send_keys("work.bishalsamanta@gmail.com")

    # wait foe 2 sec
    driver.implicitly_wait(5)

    # Wait for the button to be clickable
    wait = WebDriverWait(driver, 10)
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button/span[text()="Next"]')))

    # Click the button
    next_button.click()

    wait = WebDriverWait(driver, 10)


    # print(soup.prettify())

    # Close the browser
    driver.quit()



