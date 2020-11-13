from xueqiu_app.page.base_page import BasePage


class Search(BasePage):
    def search(self, value):
        self._param["value"] = value
        self.steps("../page/search.yaml")
