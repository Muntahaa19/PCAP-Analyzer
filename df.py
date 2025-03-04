import joblib

# Load the trained model
model = joblib.load("threat_model.pkl")

# Check feature names used in training
if hasattr(model, "feature_names_in_"):
    print("✅ Model was trained with features:")
    print(model.feature_names_in_)
else:
    print("❌ Model does not have feature_names_in_. Check training data.")
