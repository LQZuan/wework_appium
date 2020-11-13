from xueqiu_app.page.market import Market
from xueqiu_app.page.base_page import BasePage


class Main(BasePage):
    def go_to_market(self):
        # self.find(MobileBy.XPATH, '//*[@text="行情"]').click()
        self.steps("../page/main.yaml")
        return Market(self._driver)

