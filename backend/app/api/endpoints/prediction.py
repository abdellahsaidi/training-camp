from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Define the model path
MODEL_PATH = "/content/prediction_model.pkl"

# Load the model at application startup
try:
    with open(MODEL_PATH, "rb") as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    model = None
    print("Error: Model file not found. Ensure the 'prediction_model.pkl' file is in the correct location.")

# Request body schema
class SampleData(BaseModel):
    features: list[float]  # List of features for a single employee

@app.post("/predict")
async def predict(sample_data: SampleData):
    """
    Endpoint to predict employee absence or presence.
    """
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded. Please check the model file.")

    try:
        # Convert features to the required format
        features = np.array(sample_data.features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features)

        # Return the result
        if prediction[0] == 0:
            return {"status": "Absent"}
        else:
            return {"status": "Present"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")
