import urllib.request
import json

# Ort
ort = "Fulpmes"

# URL für JSON-Format
url = f"https://wttr.in/{ort}?format=j1"

# HTTP Request
response = urllib.request.urlopen(url)

# JSON-String auslesen und dekodieren
data_json = response.read().decode('utf-8')

# JSON-String ausgeben
print("🔵 Vollständiger JSON-String:")
print(data_json)

# In Python-Datenstruktur umwandeln
data = json.loads(data_json)

# Aktuelle Temperatur in Grad Celsius ausgeben
aktuelle_temp = data['current_condition'][0]['temp_C']
print(f"\n🌡️ Aktuelle Temperatur in {ort}: {aktuelle_temp}°C")
