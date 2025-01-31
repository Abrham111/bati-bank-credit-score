from rest_framework.decorators import api_view
from rest_framework.response import Response
import joblib

# Load the trained model
model = joblib.load("../models/logistic_regression.pkl")

@api_view(["POST"])
def predict_creditworthiness(request):
  try:
    # Get JSON data from request
    data = request.data 

    # Extract input values (must match feature names used during training)
    recency = data.get("Recency")
    frequency = data.get("Frequency")
    monetary = data.get("Monetary")
    stability = data.get("Stability")

    # Ensure all required fields are present
    if None in [recency, frequency, monetary, stability]:
      return Response({"error": "Missing required fields"}, status=400)

    # Make prediction
    prediction = model.predict([[recency, frequency, monetary, stability]])[0]
    prediction_text = "Good" if prediction == 1 else "Bad"

    # Return response
    return Response({"creditworthiness": prediction_text})

  except Exception as e:
    return Response({"error": str(e)}, status=500)
