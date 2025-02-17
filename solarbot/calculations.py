# solarbot/calculations.py

def calculate_solar_power(spotreba, osvit, ucinnost_panelu):
    """
    Vypočítá potřebný výkon solární elektrárny (kWp) a doporučenou kapacitu baterie (kWh).

    Parametry:
    - spotreba (float): Roční spotřeba elektřiny v kWh
    - osvit (float): Průměrný roční osvit v kWh/m²
    - ucinnost_panelu (float): Účinnost solárních panelů (např. 0.18 pro 18 %)

    Výstup:
    - (float, float, float): Potřebný výkon FVE (kWp), min. kapacita baterie (kWh), max. kapacita baterie (kWh)
    """
    if osvit <= 0 or ucinnost_panelu <= 0:
        raise ValueError("Osvit a účinnost panelů musí být kladné hodnoty.")

    vykon = spotreba / (osvit * ucinnost_panelu)
    min_baterie = vykon * 1.2
    max_baterie = vykon * 2.0
    return vykon, min_baterie, max_baterie
