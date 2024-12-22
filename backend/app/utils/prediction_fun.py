import pickle
import numpy as np
import argparse
import json
from pathlib import Path

def load_and_predict(sample_data):
    """
    Loads the machine learning model from a file and predicts if the employee
    will be absent or present based on the sample data.

    Args:
        sample_data (list): A list of features for a single employee.

    Returns:
        str: 'Absent' or 'Present' based on the model prediction.
    """
    try:
        # Define the model path
        model_path = "/content/prediction_model.pkl"

        # Load the model from the file
        with open(model_path, "rb") as model_file:
            model = pickle.load(model_file)

        # Make the prediction
        prediction = model.predict([sample_data])

        # Return the result
        if prediction[0] == 0:
            return "Absent"
        else:
            return "Present"

    except FileNotFoundError:
        return "Error: Model file not found. Ensure the 'ml_model.pkl' file is in the correct location."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if name == "main":
    # Parse arguments
    parser = argparse.ArgumentParser(description="Predict employee absence using a trained model.")
    parser.add_argument(
        "--sample_data", 
        type=str, 
        required=True, 
        help="Sample data as a JSON string representing the features of an employee."
    )
    args = parser.parse_args()

    # Load the sample data from arguments
    try:
        sample_data = json.loads(args.sample_data)
        result = load_and_predict(sample_data)
        print(f"Prediction: {result}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format for sample data.")