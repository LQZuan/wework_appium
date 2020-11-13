from page.base_page import BasePage
from page.edit_member import EditMember


class Edit(BasePage):
    def edit_member(self):
        self.steps("../page/edit.yaml")
        return EditMember(self._driver)
