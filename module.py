import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# import ChromeDriverManager


with open("config.yaml") as f:
    testdata = yaml.safe_load(f)
    service = Service(testdata['browser'])
    options = webdriver.ChromeOptions

class Site:
    def __init__(self, address):
        self.driver = webdriver.Chrome(service=service,
                                       options=options)
            # service = Service(executable_path=ChromeDriverManager().install())
            # options = webdriver.ChromeOptions()
            # self.driver = webdriver.Chrome(service=service, options=options)

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(testdata["sleep_time"])

    def find_element(self, mode, path):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)