"""Insider Test Case"""
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
width = 1400
height = 1400
driver.set_window_size(width, height)

class InsiderTestClass(unittest.TestCase):

    def test_main_page(self):
        """Insider Main Page Test"""
        driver.get("https://useinsider.com/")
        self.assertIn("Insider", driver.title, "Not Open Main Page")
        driver.find_element(By.LINK_TEXT, "Company").click()
        driver.find_element(By.LINK_TEXT, "Careers").click()

    def test_quality_assurance(self):
        """Insider All Job Click Test"""
        driver.get("https://useinsider.com/careers/quality-assurance/")
        driver.find_element(By.LINK_TEXT, "See all QA jobs").click()

    def test_job_list_detail(self):
        """Insider Filter Quality Assurance And Istanbul Turkey Test"""
        driver.get("https://useinsider.com/careers/open-positions/?department=qualityassurance")
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Accept All").click()
        time.sleep(4)
        filter_locations = driver.find_element(By.ID, "select2-filter-by-location-container")
        filter_locations.click()
        time.sleep(2)
        y_coordinate = filter_locations.location["y"]
        x_coordinate = filter_locations.location["x"]
        action = webdriver.ActionChains(driver)
        action.move_by_offset(int(x_coordinate)+200, int(y_coordinate)+100)
        action.click().perform()
        time.sleep(2)

        job_list = driver.find_elements(By.CLASS_NAME, "position-list-item")
        count = 2
        for job_detail in job_list:
            self.assertIn("Quality Assurance", job_detail.find_element(By.TAG_NAME,"span").text, "Not Quality Assurance in Job")
            self.assertIn("Istanbul, Turkey", job_detail.find_element(By.TAG_NAME,"div").text, "Not Istanbul, Turkey in Job")
            time.sleep(2)
            driver.execute_script("window.scrollTo(20, 300);")
            time.sleep(2)
            job_detail.find_element(By.TAG_NAME,"a").click()
            time.sleep(2)
            tab_len = len(driver.window_handles)
            self.assertIs(tab_len, count, "Now Open Blank Page")
            count += 1

if __name__ == "__main__":
	unittest.main()
