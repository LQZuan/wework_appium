from xueqiu_app.page.Search import Search
from xueqiu_app.page.base_page import BasePage


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)
