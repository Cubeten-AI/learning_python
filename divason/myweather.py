import requests

def get_weather(city):
    api_key = "69b28e9ac1534b9681f70927262907"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    
    response = requests.get(url)
    data = response.json()
    
    # Check if the API returned an error
    if "error" in data:
        print(f"Error: {data['error']['code']}: {data['error']['message']}")
        return
        
    # Extract specific data fields from the JSON
    name = data["location"]["name"]
    region = data["location"]["region"]  # This will display the state (e.g., Manipur)
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    
    # Print the formatted output
    print(f"\n--- Weather Details ---")
    print(f"Name of the city: {name}")
    print(f"State: {region}")
    print(f"Temperature: {temp_c}°C")
    print(f"Condition: {condition}")
    print(f"chance of snow: {data['current']['precip_mm']} mm")
    print(f"Humidity: {data['current']['humidity']}%")
    print(f"Wind Speed: {data['current']['wind_kph']} kph")
    print(f"Pressure: {data['current']['pressure_mb']} mb")
    print(f"Visibility: {data['current']['vis_km']} km")
    print(f"UV Index: {data['current']['uv']}")
    print(f"local time: {data['location']['localtime']}")
    print(f"-----------------------\n")
    print("Do you want another city? (yes/no): ", end="")
# Example usage:
while True:
    city_input = input("Enter the name of the city: ")
    get_weather(city_input)
    
    another = input().strip().lower()
    if another != "yes":
        break
