import urllib.request
import json

ort = "Fulpmes"
url = f"https://wttr.in/{ort}?format=j1"

response = urllib.request.urlopen(url)
data_json = response.read().decode('utf-8')
data = json.loads(data_json)

aktuelle_temp = data['current_condition'][0]['temp_C']
print(f"Aktuelle Temperatur in {ort}: {aktuelle_temp}°C")
