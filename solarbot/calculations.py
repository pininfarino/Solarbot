# solarbot/calculations.py

def calculate_solar_power(spotreba_mwh, osvit_mwh, ucinnost_panelu):
    """
    Vypočítá potřebný výkon solární elektrárny (MWp) a kapacitu baterie (MWh).

    Parametry:
    - spotreba_mwh (float): Roční spotřeba elektřiny v MWh
    - osvit_mwh (float): Průměrný roční osvit v MWh/m²
    - ucinnost_panelu (float): Účinnost panelů (např. 0.18 pro 18 %)

    Výstup:
    - (float, float, float): Potřebný výkon FVE (MWp), min. kapacita baterie (MWh), max. kapacita baterie (MWh)
    """
    if osvit_mwh <= 0 or ucinnost_panelu <= 0:
        raise ValueError("Osvit a účinnost panelů musí být kladné hodnoty.")

    vykon = spotreba_mwh / (osvit_mwh * ucinnost_panelu)  # Výpočet výkonu v MWp
    min_baterie = vykon * 1.2  # 120 % výkonu
    max_baterie = vykon * 2.0  # 200 % výkonu
    return vykon, min_baterie, max_baterie
