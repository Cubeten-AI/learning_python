import requests

def get_weather(city):
    api_key = "69b28e9ac1534b9681f70927262907"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    
    response = requests.get(url)
    data = response.json()
   
    if "error" in data:
        print(f"Error: {data['error']['message']}")
        return
        
    
    name = data["location"]["name"]
    region = data["location"]["region"]  
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    
    
    print(f"\n--- Weather Details ---")
    print(f"Name of the city: {name}")
    print(f"State: {region}")
    print(f"Temperature: {temp_c}°C")
    print(f"Condition: {condition}")
    print(f"-----------------------\n")


city_input = input("Enter the name of the city: ")
get_weather(city_input)