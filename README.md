# Project Time Estimator

Project Time Estimator is a small Flask web application and accompanying scripts that estimate the time (in days) required to complete a software project given a set of project attributes. The repository includes a trained model (model.pkl), example dataset (project_data.csv), a simple UI (index.html) for making predictions, and helper scripts for dataset generation and prediction.

## Features

- Web UI (Flask) to enter project attributes and get an estimated time in days.
- Pre-trained model (scikit-learn compatible via joblib) stored in `model.pkl`.
- Scripts to create synthetic datasets (`main2.py`) and to run predictions from the command line (`predict.py`).
- Example dataset `project_data.csv` used to train / test models.

## Files in this repository

- `app.py` - Flask application that serves `index.html` and exposes the `/predict` POST endpoint. It loads `model.pkl` with joblib and returns an estimated time.
- `index.html` - Simple HTML form for entering project attributes and showing the prediction.
- `main2.py` - Script to generate a synthetic dataset (`project_data.csv`) using a simulated formula. Modify the range or formula to generate more/less data.
- `project_data.csv` - CSV dataset with columns: `employees, complexity, experience, modules, working_hours, deadline_pressure, requirement_clarity, time_days`.
- `predict.py` - Minimal script that loads `model.pkl`, creates an example input, and prints the model's prediction.
- `model.pkl` - Trained model serialized with joblib. (Large binary file — included for inference.)

## Dataset / Columns

The project dataset (`project_data.csv`) contains the following columns used as model inputs:

- employees — Number of team members assigned to the project (integer)
- complexity — Project complexity on a scale (typically 1-10)
- experience — Average experience (years) of the team or a representative measure
- modules — Number of modules or major components to develop
- working_hours — Typical working hours per day per developer (e.g., 6-9)
- deadline_pressure — Deadline pressure level (1 - low, 3 - high)
- requirement_clarity — Clarity of requirements (1 - low, 5 - high)
- time_days — Target variable: actual/estimated time in days (integer)

The dataset included appears to be synthetic (generated via `main2.py`) and contains 500+ rows with varied parameter ranges.

## How the synthetic dataset is generated

`main2.py` creates randomized examples using ranges for each feature and a handcrafted formula to compute `time_days`:

- time_days is influenced positively by `complexity` and `modules`, and negatively by `experience` and `employees` (more people and experience reduce time).
- `deadline_pressure` and `requirement_clarity` also affect the computed time.
- The script clips values to a minimum (e.g., 10 days) and adds small random noise to simulate real measurements.

You can change the number of rows (currently set to 500 in the script) and adjust the formula to better match your domain.

## How to run the app (local)

Prerequisites:

- Python 3.8+
- pip

Setup and run:

1. Create a virtual environment (recommended):

   python -m venv venv
   source venv/bin/activate  # macOS / Linux
   venv\Scripts\activate     # Windows

2. Install required packages (Flask, pandas, scikit-learn/joblib if needed):

   pip install -r requirements.txt

   If `requirements.txt` is not present, install manually:

   pip install flask pandas scikit-learn joblib

3. Start the Flask app:

   python app.py

4. Open your browser at http://127.0.0.1:5000/ and enter the project attributes to get a prediction.

Notes:
- `app.py` expects `model.pkl` to be present in the repository root. If you re-train a model, replace this file (serialize with joblib.dump).
- For production deployment, remove `debug=True` and use a proper WSGI server (gunicorn, uWSGI) and environment variables.

## How to run prediction from command line

The `predict.py` script demonstrates loading the model and predicting for a hard-coded example input. To try your own inputs, modify the `input_data` DataFrame in the script or adapt it to accept CLI arguments.

Example (current behavior):

   python predict.py

Output:

   Estimated Project Time: <N> days

## Training a model (notes)

This repository does not currently include the training script used to produce `model.pkl`. If you want to train your own model from `project_data.csv`, a simple workflow is:

1. Load the CSV with pandas:

   df = pd.read_csv("project_data.csv")

2. Split into X (features) and y (time_days).

3. Use scikit-learn (e.g., RandomForestRegressor, GradientBoostingRegressor, or LinearRegression) to train and evaluate.

4. Save the trained model with joblib:

   joblib.dump(model, "model.pkl")

Consider standard practices: cross-validation, scaling if needed, hyperparameter tuning, and checking feature importance.

## Example inputs and expected ranges

- employees: 2–10
- complexity: 1–10
- experience: 1–10 (years)
- modules: 4–20
- working_hours: 6–9
- deadline_pressure: 1–3
- requirement_clarity: 1–5

These ranges reflect how `main2.py` generates data; if you use real project data, ensure values are normalized to the same scales or retrain the model.

## Suggestions & Next steps

- Add a `requirements.txt` listing dependencies.
- Add a training script (e.g., `train.py`) that reads `project_data.csv`, trains a model, evaluates it, and stores `model.pkl` with reproducible seed.
- Add unit tests and simple CI to ensure the web app runs.
- Improve UI to include validation and explanations for input fields.
- Consider serializing model metadata (features order, version) so `app.py` and `predict.py` remain compatible after retraining.

## Contributing

Contributions are welcome. Suggested contribution workflow:

- Fork the repository
- Create a branch for your feature/fix
- Submit a pull request with a clear description and tests where appropriate

## License

If you have a preferred license, add a LICENSE file. Otherwise, consider permissive licenses such as MIT.

## Contact

For questions or help, open an issue on the repository or reach out to the repository owner.
