from flask import Flask, render_template, request

# Create the Flask app
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')  # Renders the index.html file

# Route for handling form submissions
@app.route('/predict', methods=['POST'])
def predict():
    # Example: Fetch data from the form
    user_input = request.form.get('data')
    # Placeholder for prediction logic
    prediction = f"Your input was: {user_input}"  # Dummy prediction
    return render_template('result.html', prediction=prediction)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
