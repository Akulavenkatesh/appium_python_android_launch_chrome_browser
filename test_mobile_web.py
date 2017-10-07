import unittest
from time import sleep
from appium import webdriver
import desired_capabilities


class TestMobileWeb(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        desired_caps = desired_capabilities.get_desired_capabilities()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def testmobileweb(self):
        self.driver.get('https://www.exploretrip.com/')
        sleep(15)
