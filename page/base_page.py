from typing import List

import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _black_list = []
    _error_count = 0
    _error_max = 10
    _param = {}

    def __init__(self, driver: WebDriver=None):
        self._driver = driver

    """处理死循环的情况"""
    def find(self, by, locator=None):
        try:
            # TODO:为什么yaml的by的值是xpath，find_element可以接收呢？locator不是带“”的值，也可以接收
            """
            跟到代碼中的By，其實這個類中也就是定義了一些常量，ID='id',XPATH='xpath'，所以這裡就可以直接用xpath。
            而locator在yaml中定义，其实就是个字符串，取出来也是字符串。所以也就不存在说传过来的参数不带引号的说法了
            """
            # TODO:举个例子来理解这个接收tuple
            element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by,
                                                                                                             locator)
            self._error_count = 0
            return element
        except Exception as e:
            """每次循环加1"""
            self._error_count += 1
            """如果错误次数大于10，则直接抛出异常"""
            if self._error_count >= self._error_max:
                raise e
            """
            这里需要定义一个black_list,存储可能弹框的元素。
            遍历black_list，看看是否存在black_list中的元素。
            如果存在，那么直接点击第一个，然后弹框就可以去掉，接着继续查找需要找的元素。
            如果页面也没有找到black list元素，那么抛出异常。
            """
            # TODO:这里真的会存在死循环的情况吗？我感觉不存在
            for black in self._black_list:
                elements = self._driver.find_elements(black)
                if len(elements) > 0:
                    elements[0].click()
                    """这个return必须放在if里面，不然，如果第一次遍历没找着也会return跳出循环"""
                    return self.find(by, locator)

            raise e

    def send(self, value, by, locator=None):
        try:
            self.find(by, locator).send_keys(value)
            self._error_count = 0
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.send(value, by, locator)
            raise e

    """读取并处理yaml"""

    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            """将文件load到一个变量中"""
            steps: List[dict] = yaml.safe_load(f)
            """处理这个yaml"""
            for step in steps:
                """如果这个dict中有by，那么查找元素"""
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                    # self._driver.find_element(MobileBy.XPATH, '//*[@text="行情"]')
                """如果这个dict中有action，那么执行操作"""
                if "action" in step.keys():
                    if "click" == step["action"]:
                        element.click()
                        """如果是send action，需要先取出需要发送的内容"""
                    elif "send" == step["action"]:
                        """
                        比如content yaml中定义的是"{value}"，content={value}
                        如果value跟param相等，那么
                        """
                        # TODO:不太理解
                        content: str = step["value"]
                        for param in self._param:
                            content = content.replace("{%s}" % param, self._param[param])
                        self.send(content, step["by"], step["locator"])
