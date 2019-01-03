from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class testc1(unittest.TestCase):
    def testdf1(self):
        self.driver = webdriver.Firefox()

    def testdf2(self):
        driver = self.driver
        driver.get("http://172.17.12.50/CodelogixTest/Default.aspx")

    def testdf3(self):
        driver = self.driver
        self.elem = driver.find_element_by_xpath('//*[@id="user"]')
        self.elem.send_keys("coder_1")
        self.elem = driver.find_element_by_xpath('//*[@id="pw"]')
        self.elem.send_keys("Test@123")
        self.elem = driver.find_element_by_xpath('//*[@id="checkUsrLogin"]').click()

uni = testc1()
uni.testdf1()
uni.testdf2()
uni.testdf3()

print('hi vhohgi')



print()

