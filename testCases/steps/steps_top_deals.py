from pytest_bdd import scenario, then, parsers
from configurations.context import Context
from pageObjects.offersPage import OffersPage
from testCases.common_steps.steps_common import *
from utils.fileReader import get_feature_file_path


@when(parsers.cfparse('I search for vegetable "{tomato}"'))
def search_for_tomato(tomato):
    offers_page = OffersPage()
    offers_page.search_for_vegetable(vegetable_name=tomato)
    Context.offers_page = offers_page


@then(
    parsers.cfparse('I verify "{tomato}", "{price:Number}" and "{discount_price:Number}"', extra_types={"Number": int}))
def verify_tomato_is_selected(tomato, price, discount_price):
    offers_page = Context.offers_page
    name = offers_page.get_vegetable_name()
    _price = offers_page.get_vegetable_price()
    disc_price = offers_page.get_vegetable_discount_price()
    assert name == tomato
    assert _price == price
    assert disc_price == discount_price


@when(parsers.cfparse('I search for vegetable "{wheat}"'))
def search_for_wheat(wheat):
    offers_page = OffersPage()
    offers_page.search_for_vegetable(vegetable_name=wheat)
    Context.offers_page = offers_page


@then(
    parsers.cfparse('I verify "{wheat}", "{price:Number}" and "{discount_price:Number}"', extra_types={"Number": int}))
def verify_wheat_is_selected(wheat, price, discount_price):
    offers_page = Context.offers_page
    name = offers_page.get_vegetable_name()
    _price = offers_page.get_vegetable_price()
    disc_price = offers_page.get_vegetable_discount_price()
    assert name == wheat
    assert _price == price
    assert disc_price == discount_price


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
