from page.base_page import BasePage
from page.persional_info import PersonalInfo


class Search(BasePage):
    def search(self):
        self._param["value"] = "hg02"
        self.steps("../page/search.yaml")

        return PersonalInfo(self._driver)