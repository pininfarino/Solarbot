import streamlit as st
from solarbot.data import get_solar_irradiance
from solarbot.calculations import calculate_solar_power

# Titulek aplikace
st.title('Solarbot – Kalkulačka solární elektrárny')

# Vstupní formulář
spotreba = st.number_input('Zadejte roční spotřebu elektřiny (v kWh):', min_value=0.0)
okres = st.selectbox('Vyberte váš okres:', ['Praha', 'Brno', 'Ostrava', 'Plzeň', 'Liberec'])
ucinnost_panelu = st.slider('Zadejte účinnost panelů (%):', min_value=10, max_value=25, value=18)

# Výpočet
if spotreba > 0 and okres:
    osvit = get_solar_irradiance(okres)
    vykon, min_baterie, max_baterie = calculate_solar_power(spotreba, osvit, ucinnost_panelu / 100)

    # Výstup výsledků
    st.subheader('Výsledky:')
    st.write(f'**Potřebný výkon FVE:** {vykon:.2f} kWp')
    st.write(f'**Doporučená kapacita baterie:** {min_baterie:.2f} kWh až {max_baterie:.2f} kWh')
