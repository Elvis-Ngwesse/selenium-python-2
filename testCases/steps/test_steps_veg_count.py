import os
from pytest_bdd import scenario, given, when, then
from configurations.context import Context
from pageObjects.greenKartPage import GreenKartPage
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), "../.."))
FEATURE_FILE = os.path.join(ROOT_DIR, f"testCases/features/vegetable_count.feature")


@scenario(FEATURE_FILE, 'Verify brocolli count')
@given('I navigate to GreenKart Page')
def test_navigate_to_brocolli_green_kart_page():
    green_kart_page = GreenKartPage()
    Context.green_kart_page = green_kart_page


@when('I increase vegetable quantity count')
def i_increase_count():
    green_kart_page = Context.green_kart_page
    _brocolli = 'brocolli'
    results = green_kart_page.increase_item_quantity(_brocolli, _index=1, times=2)
    Context.results = results


@then('I verify quantity is correct')
def i_verify_results():
    results = Context.results
    assert results == 3



@scenario(FEATURE_FILE, 'Verify cauliflower count')
@given('I navigate to GreenKart Page')
def test_navigate_to_cauliflower_green_kart_page():
    green_kart_page = GreenKartPage()
    Context.green_kart_page = green_kart_page


@when('I increase vegetable quantity count')
def i_increase_count():
    green_kart_page = Context.green_kart_page
    _brocolli = 'cauliflower'
    results = green_kart_page.increase_item_quantity_by_double_clicking(_brocolli, _index=2, times=2)
    Context.results = results


@then('I verify quantity is correct')
def i_verify_results():
    results = Context.results
    assert results == 5