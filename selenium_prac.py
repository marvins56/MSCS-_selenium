from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Deprecated - no longer needed
# This path for the ChromeDriver is no longer used in the current implementation
chrome_driver_path = "/Users/philippmuellauer/Development/chromedriver"

# Initialize Chrome options
chrome_options = webdriver.ChromeOptions()
# Add an experimental option to keep the Chrome browser open after the script finishes
chrome_options.add_experimental_option("detach", True)

# Initialize the Chrome WebDriver with the specified options
# This line is the actual driver initialization using the previously set chrome_options
driver = webdriver.Chrome(options=chrome_options)

# Define a function to test various components on a web page
def test_eight_components():
    # Navigate to a specific URL
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    # Retrieve and check the title of the web page
    title = driver.title
    assert title == "Web form"

    # Set an implicit wait time for elements to become available
    driver.implicitly_wait(0.5)

    # Locate the text box by its name and store it
    text_box = driver.find_element(by=By.NAME, value="my-text")
    # Locate the submit button using a CSS selector and store it
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # Input text into the text box
    text_box.send_keys("Selenium")
    # Click the submit button
    submit_button.click()

    # Locate the message element by its ID and retrieve its text
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    # Assert that the message text is as expected
    assert value == "Received!"

    # Close the current browser window
    # Uncomment the next line to close all browser windows and end the session
    # driver.quit()
    driver.close()

# Execute the test function
test_eight_components()
