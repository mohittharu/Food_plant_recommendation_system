import joblib
import numpy as np

# Load model and scaler
model = joblib.load("src/Classifier/Random_forest_v1.joblib")
scaler = joblib.load("src/Classifier/Scaler_1.joblib")

def predict(input_data: list):
    """
    input_data: list of numeric features in correct order
    returns: prediction, confidence
    """
    input_features = np.array([input_data])
    input_scaled = scaler.transform(input_features)

    prediction = model.predict(input_scaled)[0]
    probabilities = model.predict_proba(input_scaled)[0]
    confidence = float(np.max(probabilities))

    return prediction, confidence


# Optional local test
if __name__ == "__main__":
    sample_input = [6.5, 1.2, 45, 120, 30]
    pred, conf = predict(sample_input)
    print(pred, conf)
