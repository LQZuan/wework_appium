from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestContact:
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
        pass

    def test_contact(self):
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[@resource-id="com.tencent.wework:id/dqn" and contains(@text, "通讯录")]').click()
        # 滚动添加
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        # 手动添加
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="必填"]').send_keys('hg02')
        self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手机号"]').send_keys('13800138001')
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # sleep(2)
        # print(self.driver.page_source)
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert result == "添加成功"


