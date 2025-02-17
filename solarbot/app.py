import streamlit as st
from calculations import calculate_solar_power  # Import výpočetní logiky
import matplotlib.pyplot as plt

# 🔆 Průměrný roční osvit pro jednotlivé okresy (hodnoty v MWh/m²/rok)
SOLAR_IRRADIANCE = {
    'Praha': 1.05,  # 1050 kWh/m²/rok → 1.05 MWh/m²/rok
    'Brno': 1.02,
    'Ostrava': 1.00,
    'Plzeň': 1.03,
    'Liberec': 0.98
}

# 🌞 Titulek aplikace
st.title('🌞 Solarbot')
st.subheader('Výpočet solární elektrárny a baterie')

# 🔢 Uživatelský vstup
spotreba_mwh = st.number_input('🔋 Zadejte roční spotřebu elektřiny (v MWh):', min_value=0.0)
okres = st.selectbox('📍 Vyberte váš okres:', list(SOLAR_IRRADIANCE.keys()))
ucinnost_panelu = st.slider('⚡ Zadejte účinnost panelů (%):', min_value=10, max_value=25, value=18)

# 📊 Výpočet a výstup
if spotreba_mwh > 0 and okres:
    osvit_mwh = SOLAR_IRRADIANCE[okres]
    ucinnost = ucinnost_panelu / 100  # Převod na desetinné číslo
    vykon, min_baterie, max_baterie = calculate_solar_power(spotreba_mwh, osvit_mwh, ucinnost)

    st.subheader('✅ Výsledky:')
    st.write(f'**🔆 Potřebný výkon FVE:** `{vykon:.3f} MWp`')
    st.write(f'**🔋 Doporučená kapacita baterie:** `{min_baterie:.3f} MWh` až `{max_baterie:.3f} MWh`')


st.write("")
st.write("")

# 🌞 Titulek aplikace
st.title('🌞 Solarbot – Osvit v ČR')

# 📊 Vykreslení grafu pomocí Matplotlib
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(SOLAR_IRRADIANCE.keys(), SOLAR_IRRADIANCE.values(), color='orange')

# Popisky
ax.set_xlabel("Město")
ax.set_ylabel("Průměrný roční osvit (MWh/m²)")
ax.set_title("Průměrný roční osvit v MWh/m² pro vybraná města")
ax.set_ylim(0.9, 1.1)  # Nastavení rozmezí osy Y pro lepší viditelnost rozdílů
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 📊 Zobrazení grafu ve Streamlit
st.pyplot(fig)

st.write("")
st.write("")

# 🔗 Přidání odkazu na GitHub
st.markdown("[📌 Zdrojový kód na GitHubu](https://github.com/pininfarino/Solarbot)", unsafe_allow_html=True)