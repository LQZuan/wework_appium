from page.base_page import BasePage
from page.confirm import Confirm


class EditMember(BasePage):
    def del_member(self):
        self.steps("../page/del.yaml")
        return Confirm(self._driver)
