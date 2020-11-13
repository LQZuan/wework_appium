from xueqiu_app.page.app import App


class TestSearch:
    def test_search(self):
        App().start().main().go_to_market().goto_search().search("jd")
