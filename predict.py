import joblib
import pandas as pd

model = joblib.load("model.pkl")

# Use DataFrame with column names
input_data = pd.DataFrame([[5, 7, 3, 10, 8, 2, 4]], columns=[
    "employees", "complexity", "experience", "modules",
    "working_hours", "deadline_pressure", "requirement_clarity"
])

prediction = model.predict(input_data)

print("Estimated Project Time:", int(prediction[0]), "days")