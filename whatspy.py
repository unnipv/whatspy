# This is the main module that provides the core functionality for interacting with WhatsApp Web.
# It contains main class or functions that handle the automation of WhatsApp Web using Selenium.


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://web.whatsapp.comwhatsapp_wrapper/")