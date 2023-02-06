import os
from pytest_bdd import scenario, given, when, then, parsers
from configurations.context import Context
from pageObjects.greenKartPage import GreenKartPage
from pageObjects.offersPage import OffersPage

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), "../.."))
FEATURE_FILE = os.path.join(ROOT_DIR, f"testCases/features/top_deals.feature")


@scenario(FEATURE_FILE, 'Search for tomato deal')
@given('I navigate to GreenKart Page')
def test_navigate_to_tomato_green_kart_page():
    green_kart_page = GreenKartPage()
    Context.green_kart_page = green_kart_page


@when('I click on top deals')
def click_on_top_deals():
    green_kart_page = Context.green_kart_page
    green_kart_page.click_on_top_deals()


@when('I navigate to offers page')
def navigate_to_offers_page():
    green_kart_page = Context.green_kart_page
    green_kart_page.navigate_to_offers_page()


@when(parsers.cfparse('I search for vegetable "{tomato}"'))
def search_for_vegetable(tomato):
    offers_page = OffersPage()
    offers_page.search_for_vegetable(vegetable_name=tomato)
    Context.offers_page = offers_page


@then(
    parsers.cfparse('I verify "{tomato}", "{price:Number}" and "{discount_price:Number}"', extra_types={"Number": int}))
def verify_selected_vegetable(tomato, price, discount_price):
    offers_page = Context.offers_page
    name = offers_page.get_vegetable_name()
    _price = offers_page.get_vegetable_price()
    disc_price = offers_page.get_vegetable_discount_price()
    assert name == tomato
    assert _price == price
    assert disc_price == discount_price


@scenario(FEATURE_FILE, 'Search for wheat deal')
@given('I navigate to GreenKart Page')
def test_navigate_to_wheat_green_kart_page():
    green_kart_page = GreenKartPage()
    Context.green_kart_page = green_kart_page


@when('I click on top deals')
def click_on_top_deals():
    green_kart_page = Context.green_kart_page
    green_kart_page.click_on_top_deals()


@when('I navigate to offers page')
def navigate_to_offers_page():
    green_kart_page = Context.green_kart_page
    green_kart_page.navigate_to_offers_page()


@when(parsers.cfparse('I search for vegetable "{tomato}"'))
def search_for_vegetable(tomato):
    offers_page = OffersPage()
    offers_page.search_for_vegetable(vegetable_name=tomato)
    Context.offers_page = offers_page


@then(
    parsers.cfparse('I verify "{wheat}", "{price:Number}" and "{discount_price:Number}"', extra_types={"Number": int}))
def verify_selected_vegetable(wheat, price, discount_price):
    offers_page = Context.offers_page
    name = offers_page.get_vegetable_name()
    _price = offers_page.get_vegetable_price()
    disc_price = offers_page.get_vegetable_discount_price()
    assert name == wheat
    assert _price == price
    assert disc_price == discount_price


@scenario(FEATURE_FILE, 'View offers')
@given('I navigate to GreenKart Page')
def test_navigate_offers_to_green_kart_page():
    green_kart_page = GreenKartPage()
    Context.green_kart_page = green_kart_page


@when('I click on top deals')
def click_on_top_deals():
    green_kart_page = Context.green_kart_page
    green_kart_page.click_on_top_deals()


@when('I navigate to offers page and back')
def navigate_to_offers_page():
    green_kart_page = Context.green_kart_page
    url = green_kart_page.navigate_to_offers_page_and_back()
    Context.url = url


@then('I verify page url')
def verify_page_url():
    offers_page_url = "https://rahulshettyacademy.com/seleniumPractise/#/offers"
    url = Context.url
    assert url == offers_page_url
