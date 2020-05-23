import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from page_object.home_page import HomePage
from utilites.baseclass import BaseClass

# @pytest.mark.usefixtures("setup")



class TestOne(BaseClass):
    def test_e2e(self):
        log=self.getLogger()
        home_page=HomePage(self.driver)
        # title of Homepage
        actual_title = self.driver.title
        log.info("verify the title")
        # validate title of HomePage
        assert actual_title == 'Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!', print(
            "-------->test case failed: unable to validate title of home page")
        log.info("Title of Homepage ------>"+ actual_title+ "--------->test case passed")
        log.info("title verified")
        # handle html popup
        home_page.close_popup().click()
        # mosehover
        home_page.moverhover_electronic_operation()
        # select Samsung S10 Lite
        home_page.select_samsungs10().click()
        # verify Samsung S10 Lite page
        time.sleep(3)
        samsungLite_page = self.driver.title
        assert 'Samsung S10 lite - Buy svnbvamsung S10 lite Online at Low Prices In India | Flipkart.com' == samsungLite_page, print(
            "unable to validate Clock page")
        log.info("Verified page expected title :"+ samsungLite_page)


