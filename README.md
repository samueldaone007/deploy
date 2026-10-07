# Student Stress Predictor

A simple Streamlit web app that predicts a student's stress level from six daily-life
factors using a machine learning model (`RandomForestClassifier`) serialized with Joblib.

## Features

- **Interactive sliders** for the six input features:
  1. Study hours per day
  2. Extracurricular hours per day
  3. Sleep hours per day
  4. Social hours per day
  5. Physical activity hours per day
  6. Grades
- **One-click prediction** — returns the predicted stress level class.
- **Custom background image** rendered via base64-encoded CSS.

## Project Structure

```
.
├── deploy/
│   ├── images1.jpg                  # background image
│   ├── requirements.txt
│   ├── stress_student.py            # app (loads model from deploy/)
│   └── Student_Stress_Predictor.pkl # trained model
├── images1.jpg
├── requirements.txt
├── stress_student.py                # app (loads model from repo root)
└── Student_Stress_Predictor.pkl
```

> The repo contains two near-identical copies of the app. Run the one that matches
> the directory you launch from — each script resolves the model path differently.

## Requirements

- Python 3.8+
- Dependencies (see `requirements.txt`):

```
numpy
streamlit
joblib
scikit-learn
```

## Installation

```bash
git clone <repo-url>
cd deploy
pip install -r requirements.txt
```

## Usage

From the repository root:

```bash
streamlit run stress_student.py
```

Or from inside the `deploy/` folder:

```bash
cd deploy
streamlit run stress_student.py
```

Then open the URL printed in the terminal (default `http://localhost:8501`), set the
six sliders, and click **Predict Stress Level**.

## How It Works

1. The app loads `Student_Stress_Predictor.pkl` with `joblib.load()`.
2. Slider values are collected into a single feature row: `[study, extracurricular, sleep, social, physical, grades]`.
3. `model.predict()` returns the stress-level class, which is rendered in the UI.

The feature order above must match the column order used during training; changing it
will silently produce wrong predictions.

## Notes

- The training code/notebook is not included in this repository — only the serialized
  model is shipped. Retraining requires the original dataset.
- Pickle (`.pkl`) files can only be loaded safely if you trust their source, and they
  are tied to the scikit-learn version they were created with.

## Disclaimer

This tool is for educational/demonstration purposes only. It is **not** a medical or
psychological diagnostic instrument and should not be used to make decisions about a
real student's mental health. If you are struggling with stress, please reach out to a
qualified professional or your school's counseling service.
