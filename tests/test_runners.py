import pytest
from resources.page_object import PageActions
test = PageActions()


class TestEcommerce:
    @pytest.mark.regression
    def test_setup(self):
        test.setup()

    @pytest.mark.regression
    def test_get_product_detail_page(self):
        test.get_product_detail_page()

    @pytest.mark.regression
    def test_select_product(self):
        test.select_product()

    @pytest.mark.smoke
    def test_fill_payment_details(self):
        test.fill_payment_details()

    @pytest.mark.smoke
    def test_complete_order(self):
        test.complete_order()
