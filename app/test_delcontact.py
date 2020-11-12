from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDelContact:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['noReset'] = 'true'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(15)

    def teardown(self):
        self.driver.quit()

    def test_contact(self):
        # 删除成员
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[@resource-id="com.tencent.wework:id/dqn" and contains(@text, "通讯录")]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/guu"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="搜索"]').send_keys('hg02')
        self.driver.find_element(MobileBy.XPATH, '//*[@text="Abc"]/..//*[@text="hg02"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/guk"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="确定"]').click()
        result = self.driver.find_element(MobileBy.XPATH, '//*[@text="无搜索结果"]').text
        assert "无搜索结果" == result


