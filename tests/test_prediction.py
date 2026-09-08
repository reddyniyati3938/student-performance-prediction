import joblib
import pandas as pd


def test_model_prediction():
    model = joblib.load("models/student_performance_model.joblib")

    sample = pd.DataFrame([{
        "school": "GP",
        "sex": "F",
        "age": 19,
        "address": "U",
        "famsize": "GT3",
        "Pstatus": "T",
        "Medu": 4,
        "Fedu": 4,
        "Mjob": "at_home",
        "Fjob": "other",
        "reason": "course",
        "guardian": "mother",
        "traveltime": 4,
        "studytime": 4,
        "failures": 0,
        "schoolsup": "yes",
        "famsup": "yes",
        "paid": "yes",
        "activities": "yes",
        "nursery": "yes",
        "higher": "yes",
        "internet": "yes",
        "romantic": "no",
        "famrel": 5,
        "freetime": 5,
        "goout": 5,
        "Dalc": 1,
        "Walc": 3,
        "health": 5,
        "absences": 5
    }])

    prediction = model.predict(sample)[0]

    assert 0 <= prediction <= 20