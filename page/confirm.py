from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class Confirm(BasePage):
    def confirm(self, delMember):
        self.steps("../page/confirm.yaml")
        sleep(5)
        ele = self._driver.find_elements(MobileBy.XPATH, f'//*[@text="Abc"]/..//*[@text="{delMember}"]')
        # TODO:为什么下面这种方式找不到呢？
        # ele = self.find((MobileBy.XPATH, '//*[@text="Abc"]/..//*[@text="hg02"]'))
        if len(ele) > 0:
            return False
        else:
            return True
