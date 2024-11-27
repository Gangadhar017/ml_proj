from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

# Load the saved model and scaler
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        form_data = request.form
        input_data = {
            "age": int(form_data['age']),
            "cigsPerDay": float(form_data['cigsPerDay']),
            "totChol": float(form_data['totChol']),
            "sysBP": float(form_data['sysBP']),
            "diaBP": float(form_data['diaBP']),
            "BMI": float(form_data['BMI']),
            "heartRate": float(form_data['heartRate']),
            "glucose": float(form_data['glucose'])
        }

        # Convert the input to a pandas DataFrame
        input_df = pd.DataFrame([input_data])

        # Scale the input data
        scaled_data = scaler.transform(input_df)

        # Predict the CVD risk
        prediction = model.predict(scaled_data)
        risk_score = model.predict_proba(scaled_data)[:, 1]

        # Return the results to the user
        return render_template(
            'result.html',
            risk=int(prediction[0]),
            risk_score=round(float(risk_score[0]) * 100, 2)
        )

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
