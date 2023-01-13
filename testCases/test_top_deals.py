from pageObjects.greenKartPage import GreenKartPage
from pageObjects.offersPage import OffersPage


class TestSearchTopDeals:

    def test_search_tomato_deal(self):
        green_kart_page = GreenKartPage()
        tomato = 'Tomato'
        green_kart_page.click_on_top_deals()
        green_kart_page.navigate_to_offers_page()
        offers_page = OffersPage()
        offers_page.search_for_vegetable(vegetable_name=tomato)
        name = offers_page.get_vegetable_name()
        price = offers_page.get_vegetable_price()
        disc_price = offers_page.get_vegetable_discount_price()
        assert name == tomato
        assert price == 37
        assert disc_price == 26

    def test_search_wheat_deal(self):
        green_kart_page = GreenKartPage()
        wheat = 'Wheat'
        green_kart_page.click_on_top_deals()
        green_kart_page.navigate_to_offers_page()
        offers_page = OffersPage()
        offers_page.search_for_vegetable(vegetable_name=wheat)
        name = offers_page.get_vegetable_name()
        price = offers_page.get_vegetable_price()
        disc_price = offers_page.get_vegetable_discount_price()
        assert name == wheat
        assert price == 67
        assert disc_price == 28

    def test_view_offers(self):
        offers_page_url = "https://rahulshettyacademy.com/seleniumPractise/#/offers"
        green_kart_page = GreenKartPage()
        green_kart_page.click_on_top_deals()
        url = green_kart_page.navigate_to_offers_page_and_back()
        assert url == offers_page_url

