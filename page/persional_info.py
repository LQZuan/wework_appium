from page.base_page import BasePage
from page.edit import Edit


class PersonalInfo(BasePage):
    def goto_edit(self):
        self.steps("../page/person.yaml")
        return Edit(self._driver)
