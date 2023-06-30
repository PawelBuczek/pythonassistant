import pytest
import roman_converter

def test_VII_returns_7 ():
    assert roman_converter.convert ("VII")==7


def test_BBB_throws_error ():
    with pytest.raises(ValueError):
        assert roman_converter.convert ("BBB")
