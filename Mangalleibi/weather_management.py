import requests

api_key= "69b28e9ac1534b9681f70927262907"

def get_weather(city):
    url =  f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    try:
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            print("\nLocation not found!")
            return

        print("\n========== Weather Report ==========")
        print("City          :", data["location"]["name"])
        print("State/Region  :", data["location"]["region"])
        print("Country       :", data["location"]["country"])
        print("Local Time    :", data["location"]["localtime"])
        print("Temperature   :", data["current"]["temp_c"], "°C")
        print("Feels Like    :", data["current"]["feelslike_c"], "°C")
        print("Condition     :", data["current"]["condition"]["text"])
        print("Humidity      :", data["current"]["humidity"], "%")
        print("Wind Speed    :", data["current"]["wind_kph"], "km/h")
        print("====================================")

    except Exception as e:
        print("Error:", e)


while True:
    city = input("\nEnter City or Location: ")
    get_weather(city)

    choice = input("\nDo you want weather information for another city? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for using Weather Management System!")
        