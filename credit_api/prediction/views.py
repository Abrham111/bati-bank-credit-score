from django.shortcuts import render
import joblib
import numpy as np
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Prediction
from .serializers import PredictionSerializer

# Load models
logreg = joblib.load("../models/logistic_regression.pkl")
rf = joblib.load("../models/random_forest.pkl")

@api_view(['POST'])
def predict_creditworthiness(request):
  try:
    data = request.data  # Input JSON data
    features = np.array([data["features"]]).astype(float)  # Convert to NumPy array
    
    # Choose model based on request
    model_choice = data.get("model", "logreg")  # Default is logistic regression
    model = logreg if model_choice == "logreg" else rf
    
    prediction = model.predict(features)[0]  # Get prediction (0 = bad, 1 = good)
    
    # Save prediction to database
    prediction_entry = Prediction(input_data=data, prediction=prediction)
    prediction_entry.save()
    
    return Response({"prediction": prediction, "model_used": model_choice})
  
  except Exception as e:
    return Response({"error": str(e)}, status=400)
