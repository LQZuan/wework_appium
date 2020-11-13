from page.app import App


class TestDelContact:
    def test_delcontact(self):
        # TODO: 如何处理删除的时候，网络慢，提示正在处理的问题
        assert App().start().main().goto_contact().goto_search().search().goto_edit().edit_member().del_member().confirm()
