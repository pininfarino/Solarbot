import streamlit as st

# 🔆 Průměrné denní sluneční hodiny pro jednotlivá okresní města v ČR
SUN_HOURS_BY_LOCATION = {
    "Praha": 3.8,
    "Brno": 4.0,
    "Ostrava": 3.6,
    "Plzeň": 4.1,
    "České Budějovice": 4.2,
    "Hradec Králové": 3.9,
    "Liberec": 3.5,
    "Zlín": 3.8,
    "Olomouc": 3.7
}

def calculate_pv_bess(annual_consumption_kwh, location, self_consumption_ratio=0.7, bess_ratio=1.5, panel_efficiency=0.18):
    """
    Vypočítá optimální velikost solární elektrárny (kWp) a kapacitu baterie (kWh) na základě roční spotřeby elektřiny.

    :param annual_consumption_kwh: Roční spotřeba elektřiny v kWh
    :param location: Lokalita v ČR (ovlivňuje sluneční záření)
    :param self_consumption_ratio: Očekávané procento FV energie využité na místě (default 70 %)
    :param bess_ratio: Poměr kapacity baterie k výkonu FV systému (default 1.5:1)
    :param panel_efficiency: Účinnost solárních panelů (default 18 %)

    :return: Slovník s doporučenou kapacitou FVE a baterie
    """
    # Získání denních slunečních hodin pro lokalitu
    daily_sun_hours = SUN_HOURS_BY_LOCATION.get(location, 3.8)  # Výchozí hodnota: Praha

    # Výpočet potřebného výkonu FVE (kWp)
    required_pv_capacity_kwp = (annual_consumption_kwh * self_consumption_ratio) / (daily_sun_hours * 365 * panel_efficiency)

    # Výpočet optimální velikosti baterie (kWh)
    bess_capacity_kwh = required_pv_capacity_kwp * bess_ratio

    return {
        "Location": location,
        "Average Daily Sun Hours": daily_sun_hours,
        "Recommended PV Capacity (kWp)": round(required_pv_capacity_kwp, 2),
        "Recommended BESS Capacity (kWh)": round(bess_capacity_kwh, 2)
    }

# 🌞 Streamlit aplikace
st.title("🌞 Solarbot – Optimalizace FVE a baterie pro rodinné domy")

# 🔢 Uživatelský vstup
annual_consumption_kwh = st.number_input("🔋 Zadejte roční spotřebu elektřiny (v kWh):", min_value=1000, max_value=50000, value=5000, step=100)
location = st.selectbox("📍 Vyberte své okresní město:", list(SUN_HOURS_BY_LOCATION.keys()))
self_consumption_ratio = st.slider("⚡ Jaké procento FV energie přímo využijete?", min_value=0.5, max_value=1.0, value=0.7, step=0.05)
bess_ratio = st.slider("🔋 Poměr velikosti baterie k výkonu FV (např. 1.5:1)", min_value=0.5, max_value=2.0, value=1.5, step=0.1)

# 📊 Automatický výpočet při změně vstupních hodnot
result = calculate_pv_bess(annual_consumption_kwh, location, self_consumption_ratio, bess_ratio)

# ✅ Výstup výsledků
st.subheader("✅ Doporučené hodnoty:")
st.write(f"🔆 **Potřebný výkon FVE:** `{result['Recommended PV Capacity (kWp)']} kWp`")
st.write(f"🔋 **Doporučená kapacita baterie:** `{result['Recommended BESS Capacity (kWh)']} kWh`")
