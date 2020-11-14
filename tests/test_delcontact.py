import pytest
import yaml

from page.app import App


class TestDelContact:
    @pytest.mark.parametrize("delMember", yaml.safe_load(open("./test.yaml")))
    def test_delcontact(self, delMember):
        # delMember = "222"
        # TODO: 如何处理删除的时候，网络慢，提示正在处理的问题
        assert App().start().main().goto_contact().goto_search().search(
            delMember).goto_edit().edit_member().del_member().confirm(delMember)
