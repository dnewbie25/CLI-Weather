import json
from city import City
if __name__ == "__main__":
  med = City('Bogota')
  med.decode_url()
  # print(med.datos['json'])
  med.info_weather()
  # print(med.datos['clima'])
  print(json.dumps(med.datos, sort_keys=True, indent=4))