import joblib

print("Loading model...")

try:
    model = joblib.load("models/best_model.pkl")
    print("✅ Model loaded successfully!")
    print(type(model))
except Exception as e:
    print("❌ Error:")
    print(e)