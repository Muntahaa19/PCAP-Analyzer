import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 📌 1. Generate Sample Data (Replace with real network traffic data)
data = {
    "packet_length": np.random.randint(40, 1500, 500),
    "src_ip_count": np.random.randint(1, 100, 500),
    "dst_ip_count": np.random.randint(1, 50, 500),
    "tcp_flags": np.random.randint(0, 2, 500),
    "anomaly_score": np.random.choice([0, 1], 500, p=[0.85, 0.15])  # 0 = normal, 1 = threat
}

df = pd.DataFrame(data)

# 📌 2. Split Data
X = df.drop(columns=["anomaly_score"])  # Features
y = df["anomaly_score"]  # Labels

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 📌 3. Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 📌 4. Save Model as 'threat_model.pkl'
joblib.dump(model, "threat_model.pkl")

# 📌 5. Test Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Training Complete | Accuracy: {accuracy * 100:.2f}%")
print("✅ Model saved as 'threat_model.pkl'")
