import pytest

from constants.global_const import LANDING_PAGE, ABTESTING_PAGE
from tests.ui.test_base import BaseTest


class TestSign(BaseTest):

    @pytest.mark.ui
    def test_landing_header(self):
        assert self.pages[LANDING_PAGE].get_header_text() == 'Welcome to the-internet'

    @pytest.mark.ui
    @pytest.mark.parametrize("page_object, expected_header",
                             [(ABTESTING_PAGE, 'A/B Test Variation 1'),
                              (ABTESTING_PAGE, 'A/B Test Variation 1'),
                              (ABTESTING_PAGE, 'A/B Test Variation 1'),
                              (ABTESTING_PAGE, 'A/B Test Variation 1'),
                              (ABTESTING_PAGE, 'A/B Test Variation 1'),
                              (ABTESTING_PAGE, 'A/B Test Variation 1'),
                              (ABTESTING_PAGE, 'A/B Test Variation 1'),
                              (ABTESTING_PAGE, 'A/B Test Variation 1'),
                              (ABTESTING_PAGE, 'A/B Test Variation 1'),
                              (ABTESTING_PAGE, 'A/B Test Variation 1'),
                              (ABTESTING_PAGE, 'A/B Test Variation 1'),
                              (ABTESTING_PAGE, 'A/B Test Variation 1')]
                             )
    def test_passing_provider(self, page_object, expected_header):
        """
        Some tests could fail course the title can be changed.
        Caught two header variants: ['A/B Test Control', 'A/B Test Variation 1']
        """
        self.pages[LANDING_PAGE].click_a_b_testing_link()
        assert self.pages[page_object].get_header_text() == expected_header
