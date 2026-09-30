from temperature_log import average_temp
import pytest
from check_temperature import check




test_measurements = [{"city": "Berlin", "temperature": 20},
                    {"city":"London", "temperature": 15},
                    { "city":"Paris", "temperature": 10}]




def test_average_temp():
    assert average_temp(test_measurements) == 15, "Function 'average_temp' is not working"

def test2_average_temp():
    with pytest.raises(ValueError):
        average_temp([])

def test_check():
    results = []
    symbols = ("<", "=", ">")
    expected_results = [["Paris"], ["London"], ["Berlin"]]
    for i in symbols:
        results.append(check(test_measurements, i, 15))
    assert results == expected_results, "function 'check' is not working"

def test_empty_check(): 
    empty_check = check(test_measurements, ">", 25)
    assert empty_check == [], "function 'check' is not working for no matched results"

def test_multiple_matches():
    assert check(test_measurements, ">", 12) == ["Berlin", "London"],(
         "fuction check is not working for multiple matches ")

def test_duplications_sorting():
    test_measurements = [{"city": "Paris", "temperature": 20},
                    {"city":"Berlin", "temperature": 15},
                    { "city":"Paris", "temperature": 10}]
    assert check(test_measurements, ">", 5) == ["Berlin","Paris"]





