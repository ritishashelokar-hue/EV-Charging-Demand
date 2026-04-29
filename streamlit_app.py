import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Load ML model
model = joblib.load("EV_demand_model.pkl")

st.set_page_config(page_title="Smart EV Charging System", layout="centered")

st.title("⚡ Smart EV Charging: Demand, Cost, Time & Queue Prediction")
st.markdown("Complete EV charging station intelligence system")

# ---------------- Sidebar Inputs ----------------
st.sidebar.header("🔧 Charging Station Inputs")

hour = st.sidebar.slider("Hour of Day", 0, 23, 12)
day = st.sidebar.slider("Day of Week (1=Mon)", 1, 7, 3)
month = st.sidebar.slider("Month", 1, 12, 6)
station_id = st.sidebar.number_input("Charging Station ID", 100, 999, 101)
temperature = st.sidebar.slider("Temperature (°C)", -5, 50, 30)

sector = st.sidebar.selectbox(
    "Charging Sector",
    ["Petrol Pump", "Highway", "Shopping Mall", "Commercial Area", "Residential"]
)

charger_type = st.sidebar.radio(
    "Charger Type",
    ["Slow Charger", "Fast Charger"]
)

st.sidebar.header("🚗 Vehicle Details")

battery_capacity = st.sidebar.number_input(
    "Battery Capacity (kWh)", 10, 150, 40
)

current_charge = st.sidebar.slider(
    "Current Battery Level (%)", 0, 100, 30
)

st.sidebar.header("🚦 Queue Information")

total_chargers = st.sidebar.number_input(
    "Total Chargers at Station", 1, 20, 4
)

vehicles_in_queue = st.sidebar.number_input(
    "Vehicles Currently Waiting", 0, 50, 3
)

# ---------------- Pricing & Power ----------------
base_prices = {
    "Petrol Pump": 12,
    "Highway": 14,
    "Shopping Mall": 11,
    "Commercial Area": 10,
    "Residential": 8
}

charger_power = {
    "Slow Charger": 7,
    "Fast Charger": 50
}

input_data = np.array([[hour, day, month, station_id, temperature]])

# ---------------- Main Button ----------------
if st.button("🔮 Calculate Full Charging Details"):
    demand = model.predict(input_data)[0]

    # Price per kWh
    price_per_kwh = base_prices[sector]

    if demand > 250:
        price_per_kwh += 3
    elif demand > 150:
        price_per_kwh += 2

    if 18 <= hour <= 22:
        price_per_kwh += 2

    if charger_type == "Fast Charger":
        price_per_kwh += 4

    # Energy required
    energy_required = battery_capacity * (100 - current_charge) / 100

    # Charging time
    avg_charge_time = energy_required / charger_power[charger_type]

    # Queue waiting time
    vehicles_ahead = max(0, vehicles_in_queue - total_chargers)
    waiting_time_hours = vehicles_ahead * avg_charge_time

    wait_hr = int(waiting_time_hours)
    wait_min = int((waiting_time_hours - wait_hr) * 60)

    # Total cost
    total_cost = energy_required * price_per_kwh

    # ---------------- Output ----------------
    st.success("🔋 Charging Session Summary")

    st.write(f"⚡ Predicted Station Demand: **{int(demand)} kWh**")
    st.write(f"🔌 Charger Type: **{charger_type}**")
    st.write(f"💰 Price per kWh: **₹{price_per_kwh}**")
    st.write(f"🔋 Energy Required: **{energy_required:.2f} kWh**")
    st.write(f"⏱️ Charging Time: **{avg_charge_time:.2f} hrs**")
    st.write(f"🧾 Total Charging Cost: **₹{total_cost:.2f}**")

    st.warning("🚦 Queue Status")
    st.write(f"🚗 Vehicles Ahead: **{vehicles_ahead}**")
    st.write(f"⏳ Estimated Waiting Time: **{wait_hr} hr {wait_min} min**")

    st.success("✅ After Charging")
    st.write("🔋 Battery Level: **100%**")
    st.write("🚘 Vehicle Ready")

    # Demand trend graph
    hrs = list(range(24))
    trend = [demand + (i - hour) * 4 for i in hrs]

    plt.figure()
    plt.plot(hrs, trend)
    plt.xlabel("Hour")
    plt.ylabel("Charging Demand (kWh)")
    plt.title("Estimated Demand Trend Over the Day")
    st.pyplot(plt)
