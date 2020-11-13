from page.base_page import BasePage
from page.contact import Contact


class Main(BasePage):
    def goto_contact(self):
        self.steps("../page/main.yaml")
        return Contact(self._driver)