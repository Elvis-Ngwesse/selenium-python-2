from pageObjects.greenKartPage import GreenKartPage


class TestItemCount:

    def test_increase_brocolli_count(self):
        green_kart_page = GreenKartPage()
        _brocolli = 'brocolli'
        results = green_kart_page.increase_item_quantity(_brocolli, _index=1, times=2)
        assert results == 3

    def test_double_increase_cauliflower_count(self):
        green_kart_page = GreenKartPage()
        _brocolli = 'cauliflower'
        results = green_kart_page.increase_item_quantity_by_double_clicking(_brocolli, _index=2, times=2)
        assert results == 5
