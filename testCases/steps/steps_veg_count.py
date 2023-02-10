from pytest_bdd import when, then, scenario
from configurations.context import Context
from utils.fileReader import get_feature_file_path
from testCases.common_steps.steps_common import *
FEATURE_FILE = get_feature_file_path('vegetable_count')


@scenario(FEATURE_FILE, 'Verify brocolli count')
@when('I increase vegetable quantity count')
def increase_brocolli_count():
    green_kart_page = Context.green_kart_page
    _brocolli = 'brocolli'
    results = green_kart_page.increase_item_quantity(_brocolli, _index=1, times=2)
    Context.results = results


@then('I verify quantity is correct')
def i_verify_results():
    results = Context.results
    assert results == 3


@scenario(FEATURE_FILE, 'Verify cauliflower count')
@when('I increase vegetable quantity count')
def increase_cauliflower_count():
    green_kart_page = Context.green_kart_page
    _brocolli = 'cauliflower'
    results = green_kart_page.increase_item_quantity_by_double_clicking(_brocolli, _index=2, times=2)
    Context.results = results


@then('I verify quantity is correct')
def i_verify_results():
    results = Context.results
    assert results == 5
