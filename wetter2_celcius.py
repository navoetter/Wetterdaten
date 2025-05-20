import requests
import json

ort = "Fulpmes"
url = f"https://wttr.in/{ort}?format=j1"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    aktuelle_temp = data['current_condition'][0]['temp_C']
    print(f"Aktuelle Temperatur in {ort}: {aktuelle_temp}°C")
else:
    print("Fehler beim Abrufen der Daten")
