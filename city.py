import json
from urllib.request import urlopen

class City:
  def __init__(self, name):
    self.name = name
    self.datos = {}
    self.temperatura = float
    self.humedad = float 
    self.wind = int

  def geo_code(self,key):
    geo_code_url = f'http://api.openweathermap.org/geo/1.0/direct?q={self.name}&lang=en&appid={key}'

    self.datos['url'] = geo_code_url

  def decode_url(self):
    self.geo_code()
    url = urlopen(self.datos['url']);
    decoded_json = json.loads(url.read())
    # self.datos['json'] = json.dumps(decoded_json[0],sort_keys=True, indent=4)
    self.datos['json'] = decoded_json[0]

  def info_weather(self):
    lat = self.datos['json']['lat']
    print(f"""
    =================
    {lat}
    ================
    """)
    lon = self.datos['json']['lon']
    print(f"""
    =================
    {lon}
    ================
    """)
    weather_url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,relativehumidity_2m,windspeed_10m'
    weather_api = urlopen(weather_url)
    decoded_json = json.loads(weather_api.read())
    self.datos['clima'] = decoded_json

