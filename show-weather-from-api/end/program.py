import json
import urllib.request 

map_city_to_coords = {
    'Abuja': 'lat=9.0764785&lon=7.398574',
    'Nairobi': 'lat=-1.2920659&lon=36.8219462',
    'Accra': "lat=5.6037168&lon=-0.1869644",
}


#Modified show weather to user 
def show_weather_to_user(weather_data_list):
    output_str = ""
    for weather_data in weather_data_list:
        hour_number = weather_data['timepoint']
        temperature = weather_data['temp2m']
        output_str += f'On hour {hour_number},\n'
        if hour_number == 24:
            output_str += '(in one day)\n'
        elif hour_number == 48:
            output_str += '(in two days)\n'
        elif hour_number == 72:
            output_str += '(in three days)\n'

        output_str += f'The temperature is {temperature}\n'
        # print(output_str)
    return output_str.strip()
    
def show_weather():
    city_name = input('Please type a city')
    if city_name not in map_city_to_coords:
        print('We do not have coordinates for that city.')
    else:
        get_api_results(city_name)
        with open('api_output.json', 'r') as f:
            all_data = json.load(f)
            weather_data_list = all_data['dataseries']
        
        
        show_weather_to_user(weather_data_list)



def get_api_results(city):
    coords = map_city_to_coords[city]
    url = ('https://www.7timer.info/bin/astro.php?' + 
        f'{coords}&ac=0&unit=metric&output=json')
    results = urllib.request.urlopen(url)
    json_content = results.read().decode('utf-8')
    with open('api_output.json', 'w') as f:
        f.write(json_content)

show_weather()
