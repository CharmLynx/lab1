from lohotron import check
import pytest


def test_check_nresult():
    result = check(6)
    pytest.assertFalse(result == "neloh")