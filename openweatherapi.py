import requests



city = input("Enter a city here: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)

print(response.status_code)

if response.status_code == 200:
    print("Request successful.")
    data = response.json()
    weather = data['weather'][0]['description']
    print("Current Weather: ", weather) 
    kelvin = data["main"]["temp"]
    wind = data["wind"]["speed"]
    lat = data["coord"]["lat"]
    long = data["coord"]["lon"]
else:
   print("Oops, an error occured.")

def kelvinToFahrenheit(kelvin):
    return kelvin * 1.8 - 459.67

temperature = kelvinToFahrenheit(kelvin)
Fahrenheit = round(temperature,2)

print("Temperature (F):", Fahrenheit)
print("Windspeed: ", wind, "mph.")
print("Other Information")
print("Latitude: ", lat, "Longitude: ", long)
