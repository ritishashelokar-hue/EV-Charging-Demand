import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\programs\Project final year\data\ev_charging_processed.csv")
#
data = pd.get_dummies(data, columns=["station_id"])

#le = LabelEncoder()
#data['station_id_encoded'] = le.fit_transform(data['station_id'])

X = data.drop(columns=['charging_demand', 'station_id'])
y = data['charging_demand']
print(data.columns)  # <- see what columns are actually in your CSV


X = data.drop("charging_demand", axis=1)
y = data["charging_demand"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluation
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", mae)

# Save model
joblib.dump(model, "EV_demand_model.pkl")
print("Model saved successfully!")
