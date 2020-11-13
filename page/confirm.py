from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class Confirm(BasePage):
    def confirm(self):
        self.steps("../page/confirm.yaml")
        sleep(5)
        ele = self._driver.find_elements(MobileBy.XPATH, '//*[@text="Abc"]/..//*[@text="hg02"]')
        if len(ele) > 0:
            return False
        else:
            return True
