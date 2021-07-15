import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor

london_data_path = 'data\london_merged.csv'
london_data = pd.read_csv(london_data_path)


y = london_data.season
feature_names = ['timestamp', 'cnt', 't1', 't2', 'hum', 'wind_speed', 'weather_code', 'is_holiday', 'is_weekend']
X = london_data[feature_names]


london_model = DecisionTreeRegressor(random_state=42)
london_model.fit(X, y)


predictions = london_model.predict(X)
print(predictions)

