import requests


def get_weather(city):
    api_key = "69b28e9ac1534b9681f70927262907"  
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)
    print(response.json())

    if response.status_code == 200:
        data = response.json()

        print("City:", data["location"]["name"])
        print("Temperature:", data["current"]["temp_c"], "°C")
        print("Condition:", data["current"]["condition"]["text"])
        print("Humidity:", data["current"]["humidity"], "%")

    else:
        print("Error:", response.status_code)
        print(response.text)


city = input("Enter city name: ")
get_weather(city)
