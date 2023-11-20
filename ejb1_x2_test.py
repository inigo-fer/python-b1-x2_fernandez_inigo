from bills import *
import pytest
from util_package.bill_manager import BillManager


def create_stats_bills_EX101():
    bill_manager = BillManager()
    bills = bill_manager.create_bills_EX101()
    return Statistics(bills)


def create_stats_bills_EX102():
    bill_manager = BillManager()
    bills = bill_manager.create_bills_EX102()
    return Statistics(bills)


def create_stats_bills_EX103():
    bill_manager = BillManager()
    bills = bill_manager.create_bills_EX103()
    return Statistics(bills)


def create_stats_bills_EX104():
    bill_manager = BillManager()
    bills = bill_manager.create_bills_EX104()
    return Statistics(bills)


def test_find_top_sell_product_EX101():
    top_product = create_stats_bills_EX101().find_top_sell_product()
    assert top_product[0].product_id == "P701", "Check the function: find_top_sell_product"
    assert top_product[1] == 1, "Check the function: find_top_sell_product"


def test_find_top_sell_product_EX102():
    top_product = create_stats_bills_EX102().find_top_sell_product()
    assert top_product[0].product_id == "P702", "Check the function: find_top_sell_product"
    assert top_product[1] == 1, "Check the function: find_top_sell_product"


def test_find_top_sell_product_EX103():
    top_product = create_stats_bills_EX103().find_top_sell_product()
    assert top_product[0].product_id == "P701", "Check the function: find_top_sell_product"
    assert top_product[1] == 1, "Check the function: find_top_sell_product"


def test_find_top_sell_product_EX104():
    top_product = create_stats_bills_EX104().find_top_sell_product()
    assert top_product[0].product_id == "P704", "Check the function: find_top_sell_product"
    assert top_product[1] == 6, "Check the function: find_top_sell_product"


def test_find_top_two_sellers_EX101():
    list_sellers = create_stats_bills_EX101().find_top_two_sellers()
    assert list_sellers[0].dni == "S501", "Check the function: find_top_two_sellers"
    assert len(list_sellers) == 1, "Check the function: find_top_two_sellers"


def test_find_top_two_sellers_EX102():
    list_sellers = create_stats_bills_EX102().find_top_two_sellers()
    assert list_sellers[0].dni == "S501", "Check the function: find_top_two_sellers"
    assert len(list_sellers) == 1, "Check the function: find_top_two_sellers"


def test_find_top_two_sellers_EX103():
    list_sellers = create_stats_bills_EX103().find_top_two_sellers()
    assert list_sellers[0].dni == "S501", "Check the function: find_top_two_sellers"
    assert len(list_sellers) == 1, "Check the function: find_top_two_sellers"


def test_find_top_two_sellers_EX104():
    list_sellers = create_stats_bills_EX104().find_top_two_sellers()
    assert list_sellers[0].dni == "S502", "Check the function: find_top_two_sellers"
    assert list_sellers[1].dni == "S504", "Check the function: find_top_two_sellers"
    assert len(list_sellers) == 2, "Check the function: find_top_two_sellers"


def test_find_buyer_lowest_total_purchases_EX101():
    tuple_buyer = create_stats_bills_EX101().find_buyer_lowest_total_purchases()
    assert tuple_buyer[0].dni == "B101", "Check the function: find_buyer_lowest_total_purchases"
    assert tuple_buyer[1] == 162.5, "CCheck the function: find_buyer_lowest_total_purchases"


def test_find_buyer_lowest_total_purchases_EX102():
    tuple_buyer = create_stats_bills_EX102().find_buyer_lowest_total_purchases()
    assert tuple_buyer[0].dni == "B101", "Check find_buyer_lowest_total_purchases"
    assert tuple_buyer[1] == 498.28, "Check find_buyer_lowest_total_purchases"


def test_find_buyer_lowest_total_purchases_EX103():
    tuple_buyer = create_stats_bills_EX103().find_buyer_lowest_total_purchases()
    assert tuple_buyer[0].dni == "B102", "Check find_buyer_lowest_total_purchases"
    assert tuple_buyer[1] == 78.28, "Check find_buyer_lowest_total_purchases"


def test_find_buyer_lowest_total_purchases_EX104():
    tuple_buyer = create_stats_bills_EX104().find_buyer_lowest_total_purchases()
    assert tuple_buyer[0].dni == "B101", "Check find_buyer_lowest_total_purchases"
    assert tuple_buyer[1] == 53.5, "Check find_buyer_lowest_total_purchases"


def test_order_products_by_tax_EX101():
    list_products = create_stats_bills_EX101(
    ).order_products_by_tax(order_type=OrderType.ASC)
    assert list_products[0][0].product_id == "P701", "Check the function: order_products_by_tax"
    assert len(list_products) == 1, "Check the function: order_products_by_tax"


def test_order_products_by_tax_EX102():
    list_products = create_stats_bills_EX102(
    ).order_products_by_tax(order_type=OrderType.ASC)
    assert list_products[0][0].product_id == "P702", "Check the function: order_products_by_tax"
    assert len(list_products) == 2, "Check the function: order_products_by_tax"


def test_order_products_by_tax_EX103():
    list_products = create_stats_bills_EX103(
    ).order_products_by_tax(order_type=OrderType.ASC)
    assert list_products[0][0].product_id == "P702", "Check the function: order_products_by_tax"
    assert len(list_products) == 2, "Check the function: order_products_by_tax"


def test_order_products_by_tax_EX104():
    list_products = create_stats_bills_EX104(
    ).order_products_by_tax(order_type=OrderType.DES)
    assert list_products[0][0].product_id == "P702", "Check the function: order_products_by_tax"
    assert list_products[1][0].product_id == "P703", "Check the function: order_products_by_tax"
    assert list_products[2][0].product_id == "P704", "Check the function: order_products_by_tax"
    assert len(list_products) == 6, "Check the function: order_products_by_tax"