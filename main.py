import json
from city import City
if __name__ == "__main__":
  print("Welcome to the Weather CLI")
  key = input("Enter your OpenWeather key:\n\t")
  while True:
    city = input("Enter the city:\n\t").lower()
    country = input("Enter the country:\n\t").lower()
    info = City(city, country, key)
    info.set_temperatura()
    info.set_humidity()
    info.set_wind()
    print(f"""\n\t{city.capitalize()}, {country.capitalize()} - {info.temperatura}°C, humidy of {info.humedad}% and wind speed of {info.wind}km/h\n""")
    quit = input("Try another city?\n\t")
    if quit == "yes":
      continue 
    else:
      break
