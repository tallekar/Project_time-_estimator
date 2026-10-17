from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = pd.DataFrame([[
            int(request.form['employees']),
            int(request.form['complexity']),
            int(request.form['experience']),
            int(request.form['modules']),
            int(request.form['working_hours']),
            int(request.form['deadline_pressure']),
            int(request.form['requirement_clarity'])
        ]], columns=[
            "employees", "complexity", "experience", "modules",
            "working_hours", "deadline_pressure", "requirement_clarity"
        ])

        prediction = model.predict(data)
        result = int(prediction[0])

        return render_template("index.html", prediction_text=f"Estimated Time: {result} days")

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)