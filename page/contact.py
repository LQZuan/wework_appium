from page.Search import Search
from page.base_page import BasePage


class Contact(BasePage):
    def goto_search(self):
        self.steps("../page/contact.yaml")
        return Search(self._driver)
