from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

traveloka = "https://www.traveloka.com/en-id"

# Navigate to the website
driver.get(traveloka)

try:
    car_rental_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='product-nav']")))
    car_rental_link.find_element(By.CSS_SELECTOR, "[role='link'][href='/en-id/cars']").click()
 
    # Select tab Without Driver
    without_driver_radio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[role='radio'][name='driver']")))
    without_driver_radio.click()

    # Select Pick-up Location
    location_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
    "[data-testid='rental-search-form-location-input']")))
    location_input.click()
    location_input.send_keys("Soekarno Hatta")
    location_item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, 
    "//div[@data-testid='rental-search-form-location-item-subtitle'][contains(text(), 'Benda, Cengkareng, West Jakarta, Jakarta, Indonesia, Southeast Asia, Asia')]")))
    location_item.click()

    # Select Pick-up Date & Time
    pick_up_date_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
    "[data-testid='rental-search-form-date-input-start']")))
    pick_up_date_input.click()
    pick_up_date_item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
    "div[aria-label='calendar'] div[role='option']")))
    pick_up_date_item.click()
    pick_up_time_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
    "[data-testid='rental-search-form-time-input-start']")))
    pick_up_time_input.click()
    pick_up_time_item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
    "div[aria-label='time'] div:nth-child(14)")))
    pick_up_time_item.click()
    done_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
    "[data-testid='rental-search-form-time-confirm']")))
    done_button.click()

    # Select Drop-off Date & Time
    drop_off_date_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
    "[data-testid='rental-search-form-date-input-end']")))
    drop_off_date_input.click()
    drop_off_date_item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
    "div[aria-label='calendar'] div[role='option']")))
    drop_off_date_item.click()
    done_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
    "[data-testid='rental-search-form-time-confirm']")))
    done_button.click()

    # Click button Search Car
    search_car_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
    "[data-testid='rental-search-form-cta']")))
    search_car_button.click()

    # Select Car Provider
    driver.get("https://www.traveloka.com/en-id/car-rental/detail?sd=25-2-2024&st=9-0&ed=27-2-2024&et=9-0&driverType=WITHOUT_DRIVER&city=Soekarno%20Hatta&fromLocation=TVLK.102813.PPR_ROUTE.AIRPORT.Airport.Soekarno%20Hatta.%27%27.&productId=5036&supplierId=447&productName=Toyota%20Grand%20New%20Avanza&fromRouteId=1&toRouteId=1&searchId=d7db0901-67f9-4a7b-b7a0-1737af9c4a84")

    # Click button Continue
    continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
    "[role='button'][name='Continue']")))
    continue_button.click()
    

    # Select Pick-up Location in “Rental Office”
    pick_up_loc = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-checked='false']//div[contains(text(), 'Rental Office')]")))
    pick_up_loc.click()

    specific_location = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[img[contains(@src, 'f3ac954ccf57929e5b4f2519406ebb82')]]/div[text()='Rental Office']")))
    specific_location.click()

    pool_trac = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Pool TRAC Jakarta')]")))
    pool_trac.click()

    # Select Drop-off Location in “Other Location”
    drop_off_loc = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-checked='false']//div[contains(text(), 'Other Locations')]")))
    drop_off_loc.click()
    # Input Pick-up/Drop-off notes if needed
    pick_drop_notes_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
    "[data-testid='additional-notes']")))
    pick_drop_notes_input.send_keys("Jangan telat")

    # Click button Book Now
    book_now_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
    "[role='button'][name='Book Now']")))
    book_now_button.click()

    # Fill Contact Details
    full_name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
    "[aria-label='Full Name*']")))
    full_name_input.click()
    full_name_input.send_keys("Ewaldo Samuel")
    phone_number_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
    "[aria-label='Phone Number']")))
    phone_number_input.send_keys("83806783668")
    email_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Email*']")))
    email_input.send_keys("ewaldosamuel19@gmail.com")

    # Fill Driver Details
    driver_name_input = driver.find_element_by_css_selector("#adultForm0 [for='adultForm0'] + input")
    driver_name_input.send_keys("Ewaldo Samuel")

    driver_number_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable
    ((By.CSS_SELECTOR, "#adultForm0 [for='phoneNumber'] + input")))
    driver_number_input.send_keys("83806783668")

    driver_email_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#adultForm0 [for='emailAddress'] + input")))
    driver_email_input.send_keys("ewaldosamuel19@gmail.com")

    # Click Continue
    continue_button_2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[role='button'][name='Continue']")))
    continue_button_2.click()

    # Add a special request if needed
    special_request_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Special Requests']")))
    special_request_input.send_keys("")

    # Click Continue
    continue_button_3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[role='button'][name='Continue']")))
    continue_button_3.click()

finally:
    # Close the browser window
    driver.quit()
