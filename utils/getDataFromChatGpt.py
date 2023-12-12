from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Your login credentials
username = "your_username"
password = "your_password"


def get_data_from_chatGpt():

    # Change the URL to the desired website
    url = "https://chat.openai.com/auth/login"

    # Proxy settings
    proxy_host = "your_proxy_host"
    proxy_port = "your_proxy_port"
    proxy_username = "your_proxy_username"
    proxy_password = "your_proxy_password"

    # Open a Chrome browser with proxy settings
    options = webdriver.ChromeOptions()
    options.add_argument(f"--proxy-server={proxy_host}:{proxy_port}")
    options.add_argument(f"--proxy-auth={proxy_username}:{proxy_password}")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # Open the website
    driver.get(url)

    try:
        # Wait for the button to be clickable using data-testid
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="login-button"]'))
        )

        # Click the button
        login_button.click()

        try:
            # Replace 'your_element_locator' with the appropriate locator for an element on the next page
            element_on_next_page = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[id="username"]'))
            )

            print("Next page has loaded.")
            # Get the HTML source code of the page
            page_source = driver.page_source

            # Use BeautifulSoup to parse and print the HTML
            soup = BeautifulSoup(page_source, "html.parser")

            print(soup.prettify())
        except TimeoutException:
            print("Timed out waiting for the next page to load")
            driver.quit()
            return

    except TimeoutException:
        print("Timed out waiting for the button to be clickable")
        driver.quit()
        return

    # Wait for the page to load after clicking the button
    driver.implicitly_wait(5)
