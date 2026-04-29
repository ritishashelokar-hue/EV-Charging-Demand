import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Load data
data = pd.read_csv("data/ev_charging_full_dataset.csv")

# Encode categorical columns
le_sector = LabelEncoder()
le_charger = LabelEncoder()

data['sector'] = le_sector.fit_transform(data['sector'])
data['charger_type'] = le_charger.fit_transform(data['charger_type'])

# Features & Target
X = data.drop("charging_demand", axis=1)
y = data["charging_demand"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

# Save model & encoders
joblib.dump(model, "model/demand_model.pkl")
joblib.dump(le_sector, "model/sector_encoder.pkl")
joblib.dump(le_charger, "model/charger_encoder.pkl")

print("✅ Model trained & saved successfully!")
