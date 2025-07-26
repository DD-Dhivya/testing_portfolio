from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

#Define custom class
class logintest(unittest.TestCase):
   
   #this method runs before each test case
   def setUp(self):
      #Launch chrome browser
      self.driver = webdriver.Chrome()
      self.driver.maximize_window()
      #navigate to the login page
      self.driver.get("https://practicetestautomation.com/practice-test-login/")
    
   #This runs after each test to clean up
   def tearDown(self):
    time.sleep(1)
    self.driver.quit()
    
   #This is a positive test case using valid credentials
   def test_valid_login(self):
      driver = self.driver
      #find and fill the username field
      username = driver.find_element(By.ID, "username")
      username.send_keys("student")
      #find and fill the password
      password = driver.find_element(By.ID, "password")
      password.send_keys("Password123")
      #Click login button
      login_button = driver.find_element(By.ID, "submit")
      login_button.click()
      time.sleep(2)
      success_message = driver.find_element(By.TAG_NAME, "h1").text
      #self.assertIn to check if the expected text is present
      self.assertIn("Logged In Successfully", success_message)

    #this is a negative test case using wrong credentials
   def test_invalid_login(self):
    driver=self.driver
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    error_message = driver.find_element(By.ID, "error").text
    self.assertIn("Your username is invalid!", error_message)

# This allows you to run the tests using: python login_test.py
if __name__ == "__main__":
    unittest.main()


      


      

