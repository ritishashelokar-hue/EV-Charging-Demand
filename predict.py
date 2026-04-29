import joblib
import numpy as np

model = joblib.load("EV_demand_model.pkl")

# Input: hour, day, month, station_id, temperature
input_data = np.array([[18, 5, 6, 102, 32]])

prediction = model.predict(input_data)

print("Predicted EV Charging Demand:", int(prediction[0]), "kWh")
