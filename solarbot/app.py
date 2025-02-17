import streamlit as st

# 🔆 Průměrný roční osvit pro jednotlivé okresy (hodnoty v kWh/m²/rok)
SOLAR_IRRADIANCE = {
    'Praha': 1050,
    'Brno': 1020,
    'Ostrava': 1000,
    'Plzeň': 1030,
    'Liberec': 980
}


def calculate_solar_power(spotreba, osvit, ucinnost_panelu):
    """
    Vypočítá potřebný výkon solární elektrárny (kWp) a kapacitu baterie (kWh).

    Parametry:
    - spotreba (float): Roční spotřeba elektřiny v kWh
    - osvit (float): Průměrný roční osvit v kWh/m²
    - ucinnost_panelu (float): Účinnost panelů v desetinném tvaru (např. 0.18 pro 18 %)

    Výstup:
    - (float, float, float): Potřebný výkon FVE (kWp), min. kapacita baterie (kWh), max. kapacita baterie (kWh)
    """
    if osvit <= 0 or ucinnost_panelu <= 0:
        raise ValueError("Osvit a účinnost panelů musí být kladné hodnoty.")

    vykon = spotreba / (osvit * ucinnost_panelu)
    min_baterie = vykon * 1.2  # 120 % výkonu
    max_baterie = vykon * 2.0  # 200 % výkonu
    return vykon, min_baterie, max_baterie


# 🌞 Titulek aplikace
st.title('🌞 Solarbot – Výpočet solární elektrárny a baterie')

# 🔢 Uživatelský vstup
spotreba = st.number_input('🔋 Zadejte roční spotřebu elektřiny (v kWh):', min_value=0.0)
okres = st.selectbox('📍 Vyberte váš okres:', list(SOLAR_IRRADIANCE.keys()))
ucinnost_panelu = st.slider('⚡ Zadejte účinnost panelů (%):', min_value=10, max_value=25, value=18)

# 📊 Výpočet a výstup
if spotreba > 0 and okres:
    osvit = SOLAR_IRRADIANCE[okres]
    ucinnost = ucinnost_panelu / 100  # Převod na desetinné číslo
    vykon, min_baterie, max_baterie = calculate_solar_power(spotreba, osvit, ucinnost)

    st.subheader('✅ Výsledky:')
    st.write(f'**🔆 Potřebný výkon FVE:** `{vykon:.2f} kWp`')
    st.write(f'**🔋 Doporučená kapacita baterie:** `{min_baterie:.2f} kWh` až `{max_baterie:.2f} kWh`')
