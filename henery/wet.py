
import requests


def get_weather(city):
    api_key = "69b28e9ac1534b9681f70927262907"  # Replace
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        print("Error:", data["error"]["message"], "the given location does not exist!")
    else:
        print("\n Forecasting weather")
        print("City       :", data["location"]["name"])
        print("Region     :", data["location"]["region"])
        print("Country    :", data["location"]["country"])
        print("Temperature:", data["current"]["temp_c"], "°C")
        print("Condition  :", data["current"]["condition"]["text"])
        print("Humidity   :", data["current"]["humidity"], "%")
        print("Wind Speed :", data["current"]["wind_kph"], "km/h")
        print("Feels Like :", data["current"]["feelslike_c"], "°C")


# Main Program
city = input("Enter city name: ")
get_weather(city)