import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def setup_teardown():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def fill_form(driver, name, student_id, email, year):
    driver.find_element(By.NAME, "name").clear()
    driver.find_element(By.NAME, "name").send_keys(name)
    
    driver.find_element(By.NAME, "student_id").clear()
    driver.find_element(By.NAME, "student_id").send_keys(student_id)
    
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(email)
    
    driver.find_element(By.NAME, "year").clear()
    driver.find_element(By.NAME, "year").send_keys(year)

def test_empty_name(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")
    fill_form(driver, "", "ST101", "student@gmail.com", "3rd Year")
    driver.find_element(By.NAME, "sb").click()

def test_empty_student_id(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")
    fill_form(driver, "Harimya", "", "student@gmail.com", "3rd Year")
    # Supports both ID or Name matching depending on your preference
    driver.find_element(By.ID, "submit-btn").click()

def test_invalid_email(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")
    fill_form(driver, "Harimya", "ST101", "invalid-email", "3rd Year")
    driver.find_element(By.NAME, "sb").click()

def test_valid_registration(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")
    fill_form(driver, "Harimya", "ST101", "harimya@gmail.com", "3rd Year")
    driver.find_element(By.NAME, "sb").click()
