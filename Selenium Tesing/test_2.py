# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test5():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_5(self):
    self.driver.get("http://localhost/Hotel-Management-System/index.php")
    self.driver.set_window_size(1366, 738)
    self.driver.find_element(By.CSS_SELECTOR, ".btns:nth-child(2)").click()
    self.driver.find_element(By.NAME, "Emp_Email").click()
    self.driver.find_element(By.NAME, "Emp_Email").send_keys("Admin@gmail.com")
    self.driver.find_element(By.NAME, "Emp_Password").send_keys("1234")
    self.driver.find_element(By.NAME, "Emp_Password").send_keys("1234")
    self.driver.find_element(By.NAME, "Emp_Email").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".pagebtn:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".pagebtn:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".pagebtn:nth-child(4)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.close()
  
