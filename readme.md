# 🌞 Solarbot – Výpočet solární elektrárny a baterie

Solarbot je jednoduchá aplikace postavená na **Streamlit**, která umožňuje vypočítat optimální velikost solární elektrárny a kapacity baterie na základě zadané roční spotřeby domu a lokality.

---

## 📌 **Funkce aplikace**
- **Zadání roční spotřeby elektřiny v MWh**
- **Výběr okresu v ČR** (Praha, Brno, Ostrava, Plzeň, Liberec)
- **Výběr účinnosti solárních panelů** (10–25 %)
- **Výpočet potřebného výkonu FVE (MWp)**
- **Výpočet doporučené kapacity baterie (MWh)**

---

## 🚀 **Jak spustit aplikaci?**

### **1️⃣ Klonování repozitáře**
```bash
 git clone https://github.com/TVOJE_UZIVATELSKE_JMENO/solarbot.git
 cd solarbot
```

### **2️⃣ Instalace závislostí**
Ujisti se, že máš nainstalovaný **Python 3.10+** a virtuální prostředí:
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

### **3️⃣ Spuštění aplikace**
```bash
streamlit run solarbot/app.py
```
Aplikace poběží na **http://localhost:8501**.

---

## 📂 **Struktura projektu**
```
/Solarbot
│── /solarbot
│   │── app.py             # Hlavní Streamlit aplikace
│   │── calculations.py     # Výpočetní logika
│── requirements.txt       # Seznam závislostí
│── README.md              # Dokumentace projektu
```

---

## ⚙️ **Použité technologie**
- **Python 3.10+**
- **Streamlit** – frontend aplikace
- **Matematické výpočty výkonu FVE a baterie**

---

## 📊 **Jak funguje výpočet?**
Výpočet výkonu fotovoltaické elektrárny:
```
Výkon FVE (MWp) = Roční spotřeba (MWh) / (Průměrný osvit (MWh/m²) × Účinnost panelů)
```
Doporučená kapacita baterie:
```
Min. kapacita baterie (MWh) = Výkon FVE × 1.2
Max. kapacita baterie (MWh) = Výkon FVE × 2.0
```

---

## 🌍 **Nasazení na Streamlit Cloud**
Aplikaci lze nasadit online přes **Streamlit Community Cloud**:
1. Nahraj kód na **GitHub**
2. Přejdi na [Streamlit Cloud](https://share.streamlit.io/)
3. Propoj repozitář a nastav cestu k `app.py`
4. Klikni **„Deploy“** 🚀

---

## 📩 **Kontakt**
Pokud máš jakékoliv dotazy nebo návrhy na vylepšení, neváhej mě kontaktovat přes **GitHub Issues**.

---

🔥 **Vylepšení do budoucna:**
- 📊 **Vizualizace výroby a spotřeby elektřiny**
- 💰 **Ekonomická kalkulace návratnosti investice**
- ☀️ **Real-time data o počasí**

💡 **Chceš přidat novou funkci?** Vytvoř **Issue** nebo forkuj projekt! 🚀