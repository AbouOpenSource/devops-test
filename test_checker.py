# content of test_sample.py

from checker import checker


def test_well_format():
    assert True == checker("(())")


def test_not_well_format():
    assert checker("{}{]") == False


def test_not_well_end():
    assert checker("}}}}}}}]]]]]") == False
