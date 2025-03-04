import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset (Make sure you have a labeled dataset with 'label' column: 0 = normal, 1 = attack)
df = pd.read_csv("network_traffic.csv")

X = df.drop(columns=["label"])  # Features
y = df["label"]  # Labels

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "threat_model.pkl")  # Save model
