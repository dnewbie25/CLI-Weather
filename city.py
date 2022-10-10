import json
from urllib.request import urlopen

class City:
  def __init__(self, name, country, key):
    self.name = name
    self.country = country
    self.key = key
    self.datos = {}
    self.temperatura = float
    self.humedad = float 
    self.wind = int

  def geo_code(self):
    geo_code_url = f'http://api.openweathermap.org/geo/1.0/direct?q={self.name},{self.country}&lang=en&appid={self.key}'

    self.datos['url'] = geo_code_url

  def decode_url(self):
    self.geo_code()
    url = urlopen(self.datos['url']);
    decoded_json = json.loads(url.read())
    # self.datos['json'] = json.dumps(decoded_json[0],sort_keys=True, indent=4)
    self.datos['json'] = decoded_json[0]

  def info_weather(self):
    lat = self.datos['json']['lat']
    lon = self.datos['json']['lon']
    try:
      weather_url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,relativehumidity_2m,windspeed_10m'
      weather_api = urlopen(weather_url)
    except:
      return "not found"
    else:
      decoded_json = json.loads(weather_api.read())
      self.datos['clima'] = decoded_json
  
  def set_temperatura(self):
    self.geo_code()
    self.decode_url()
    if self.info_weather() == "not found":
      return "---"
    self.info_weather()
    self.temperatura = self.datos['clima']['hourly']['temperature_2m'][0]
  def set_humidity(self):
    self.geo_code()
    self.decode_url()
    if self.info_weather() == "not found":
      return "---"
    self.info_weather()
    self.humedad = self.datos['clima']['hourly']['relativehumidity_2m'][0]
  def set_wind(self):
    self.geo_code()
    self.decode_url()
    if self.info_weather() == "not found":
      return "---"
    self.info_weather()
    self.wind = self.datos['clima']['hourly']['windspeed_10m'][0]