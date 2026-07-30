import requests

API_KEY = "69b28e9ac1534b9681f70927262907"

def get_weather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"\nNetwork Error: {e}")
        return

    # Check if the API returned an error
    if "error" in data:
        print(f"\nError {data['error']['code']}: {data['error']['message']}")
        return

    # Extract weather information
    name = data["location"]["name"]
    region = data["location"]["region"]
    country = data["location"]["country"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    # Display weather details
    print("\n========== Weather Details ==========")
    print(f"City          : {name}")
    print(f"State         : {region}")
    print(f"Country       : {country}")
    print(f"Temperature   : {temp_c}°C")
    print(f"Condition     : {condition}")
    print(f"Precipitation : {data['current']['precip_mm']} mm")
    print(f"Humidity      : {data['current']['humidity']}%")
    print(f"Wind Speed    : {data['current']['wind_kph']} kph")
    print(f"Pressure      : {data['current']['pressure_mb']} mb")
    print(f"Visibility    : {data['current']['vis_km']} km")
    print(f"UV Index      : {data['current']['uv']}")
    print(f"Local Time    : {data['location']['localtime']}")
    print("=====================================\n")


# Main Program
while True:
    city_input = input("Enter the name of the city: ").strip()

    if city_input == "":
        print("City name cannot be empty. Please try again.\n")
        continue

    get_weather(city_input)

    # Validate user's choice
    while True:
        another = input("Do you want another city? (yes/no): ").strip().lower()

        if another == "yes":
            print()
            break

        elif another == "no":
            print("\nThank you for using the Weather App!")
            exit()

        else:
            print("Invalid choice! Please enter only 'yes' or 'no'.")