from appium import webdriver

from xueqiu_app.page.main import Main
from xueqiu_app.page.base_page import BasePage


class App(BasePage):
    """app启动"""
    def start(self):
        _app_package = 'com.xueqiu.android'
        _app_activity = '.view.WelcomeActivityAlias'
        if self._driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = _app_package
            desired_caps['noReset'] = 'true'
            desired_caps['appActivity'] = _app_activity

            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self._driver.implicitly_wait(5)

        else:
            self._driver.start_activity(_app_package, _app_activity)

        return self

    """雪球登录后首页"""
    def main(self):
        return Main(self._driver)
