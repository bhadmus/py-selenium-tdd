
import pytest
from resources.page_object import PageActions
from data_elements.element_mapper import TestData

test = PageActions()


class TestFixtureExample:
    """
    This is a fixture example
    """

    @pytest.fixture
    def setup(self):
        test.open_sauce_demo()
        yield
        test.logout()

    @pytest.mark.parametrize("user_type",
                             [
                                 TestData.standard, TestData.glitch
                             ]
                             )
    def test_standard_user(self, setup, user_type):
        test.login_user(user_type)
