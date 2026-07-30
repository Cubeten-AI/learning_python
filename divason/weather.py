import requests


def get_weather(city):
    api_key = "69b28e9ac1534b9681f70927262907"  # Replace
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)
    print(response.json())

get_weather("Shfsdfjdsiofjsdoing")

'''
Enter the name of the city: Shillong
Name: Shillong
Temperature: 15.0°C
Condition: Partly cloudy
Do you want another city? (yes/no): yes
Enter the name of the city: 
'''