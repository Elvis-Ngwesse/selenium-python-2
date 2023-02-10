from testCases.steps.steps_veg_count import *
from testCases.steps.steps_top_deals import *
top_deals_feature = get_feature_file_path('top_deals')
vegetable_count_feature = get_feature_file_path('vegetable_count')


@scenario(top_deals_feature, 'Make a new deal for tomatoes')
def test_get_tomato_deal():
    pass


@scenario(top_deals_feature, 'Make a new deal for wheat')
def test_get_wheat_deal():
    pass


@scenario(top_deals_feature, 'View offers')
def test_all_offers():
    pass


@scenario(vegetable_count_feature, 'Verify brocolli count')
def test_verify_brocolli_count():
    pass


@scenario(vegetable_count_feature, 'Verify cauliflower count')
def test_verify_cauliflower_count():
    pass
