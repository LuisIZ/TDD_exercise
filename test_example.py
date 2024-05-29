# test_example.py
from example import fetch_coordinates

def test_can_call_existing_endpoints_of_the_API():
    try:
        ret = fetch_coordinates("Lima,Peru")
        assert ret is not None, "Failed to call the existing function!"
    except Exception as e:
        assert False, f"Exception while calling an existing function: {str(e)}"

def test_cannot_call_non_existing_endpoints_of_the_API():
    try:
        ret = fetch_coordinates("something_not_existent")
        assert ret is None, "Expected None for a non-existing location"
    except AttributeError:
        pass

def test_the_result_is_correct_for_simple_cases():
    detected = fetch_coordinates("Lima,Peru")
    expected = (-12.0464, -77.0428)  # Example coordinates for Lima, Peru
    assert detected == expected, f"The result is not correct: {detected}"

def test_the_result_is_correct_for_simple_cases():
    detected = fetch_coordinates("Lima,Peru")
    expected = (-12.0464, -77.0428)  # Example coordinates for Lima, Peru
    assert detected == expected, f"The result is not correct: {detected}"
