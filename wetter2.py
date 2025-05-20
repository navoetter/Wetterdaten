import requests
import json

ort = "Fulpmes"
url = f"https://wttr.in/{ort}?format=j1"

# HTTP GET mit requests
response = requests.get(url)

if response.status_code == 200:
    data_json = response.text
    print("🔵 Vollständiger JSON-String:")
    print(data_json)

    data = json.loads(data_json)

    aktuelle_temp = data['current_condition'][0]['temp_C']
    print(f"\n🌡️ Aktuelle Temperatur in {ort}: {aktuelle_temp}°C")
else:
    print("Fehler beim Abrufen der Wetterdaten.")
