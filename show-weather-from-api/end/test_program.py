import program

def test_show_weather_to_user_single_hour():
    # Testing for a single hour data point
    weather_data_list = [{'timepoint': 1, 'temp2m': 20}]
    expected_output = "On hour 1,\nThe temperature is 20"
    assert program.show_weather_to_user(weather_data_list) == expected_output
    
def test_show_weather_to_user_multiple_hours():
    # Testing for multiple hour data points
    weather_data_list = [{'timepoint': 24, 'temp2m': 18}, {'timepoint': 48, 'temp2m': 22}]
    expected_output = "On hour 24,\n(in one day)\nThe temperature is 18\nOn hour 48,\n(in two days)\nThe temperature is 22"
    assert program.show_weather_to_user(weather_data_list) == expected_output
    
def test_show_weather_to_user_72nd_hour():
    # Testing for a data point at the 72nd hour
    weather_data_list = [{'timepoint': 72, 'temp2m': 25}]
    expected_output = "On hour 72,\n(in three days)\nThe temperature is 25"
    assert program.show_weather_to_user(weather_data_list) == expected_output
