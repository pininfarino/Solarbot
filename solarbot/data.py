# solarbot/data.py

# Hodnoty průměrného ročního osvitu v kWh/m²/rok pro jednotlivé okresy
SOLAR_IRRADIANCE = {
    'Praha': 1050,
    'Brno': 1020,
    'Ostrava': 1000,
    'Plzeň': 1030,
    'Liberec': 980
}

def get_solar_irradiance(okres):
    """Vrátí průměrný roční osvit pro daný okres."""
    return SOLAR_IRRADIANCE.get(okres, 1000)  # Výchozí hodnota 1000 kWh/m²
