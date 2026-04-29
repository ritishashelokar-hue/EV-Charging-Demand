import pandas as pd
import numpy as np

np.random.seed(42)
rows = 17578

data = {
    "hour": np.random.randint(0, 24, rows),
    "day": np.random.randint(1, 8, rows),
    "month": np.random.randint(1, 13, rows),
    "station_id": np.random.randint(100, 120, rows),
    "temperature": np.random.randint(15, 41, rows),
    "sector": np.random.choice(
        ["Petrol Pump", "Highway", "Shopping Mall", "Commercial Area", "Residential"],
        rows
    ),
    "charger_type": np.random.choice(["Fast Charger", "Slow Charger"], rows),
    "battery_capacity": np.random.randint(20, 81, rows),
    "current_charge": np.random.randint(0, 81, rows),
    "total_chargers": np.random.randint(2, 10, rows),
    "vehicles_in_queue": np.random.randint(0, 20, rows),
}

# Generate charging demand (higher in evening)
charging_demand = []
for h in data["hour"]:
    if 17 <= h <= 22:
        charging_demand.append(np.random.randint(200, 500))
    else:
        charging_demand.append(np.random.randint(50, 250))

data["charging_demand"] = charging_demand

df = pd.DataFrame(data)

# Create data folder if not exists
import os
os.makedirs("data", exist_ok=True)

df.to_csv("data/ev_charging_full_dataset.csv", index=False)

print("✅ ev_charging_full_dataset.csv generated successfully!")
