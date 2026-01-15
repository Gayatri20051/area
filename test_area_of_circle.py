from area_of_circle import area_of_circle

def test_area_of_circle_basic():
    assert area_of_circle(1) == 3.14

def test_area_of_circle_integer():
    assert round(area_of_circle(3), 2) == 28.26

def test_area_of_circle_float():
    assert area_of_circle(2.5) == 19.625
