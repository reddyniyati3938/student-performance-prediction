# Student Performance Prediction

## Project Overview

This project predicts a student's final academic grade using student-related information such as study time, previous failures, family support, absences, and other demographic and social factors.

The project uses the UCI Student Performance dataset and a Random Forest Regression model.

## Dataset

The dataset contains information about students and their academic performance.

The target variable is:

* `G3` - Final grade

The model does not use `G1` and `G2` as input features because they are earlier grades and are strongly related to the final grade.

## Features

* Load and preprocess student performance data
* Encode categorical features using One-Hot Encoding
* Train a Random Forest Regression model
* Evaluate the model using MAE, RMSE, and R²
* Save and load the trained model using Joblib
* Accept student information through the command line
* Validate user inputs
* Predict the student's final grade on a 0–20 scale
* Test the prediction functionality using Pytest

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Joblib
* Pytest

## Project Structure

student-performance-prediction/
├── data/
│   └── student_performance.csv
├── models/
│   └── student_performance_model.joblib
├── src/
│   ├── data_preprocessing.py
│   ├── train_model.py
│   └── predict.py
├── tests/
│   └── test_prediction.py
├── .gitignore
├── README.md
├── requirements.txt
└── statement.md

## Installation

Create and activate a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required libraries.

```bash
pip install -r requirements.txt
```

## Data Preprocessing

Run:

```bash
python src/data_preprocessing.py
```

## Train the Model

Run:

```bash
python src/train_model.py
```

The trained model is saved as:

```text
models/student_performance_model.joblib
```

## Make a Prediction

Run:

```bash
python src/predict.py
```

The program asks for student information through the command line and predicts the student's final grade.

## Model Evaluation

The current model produced:

* Mean Absolute Error (MAE): 2.966
* Root Mean Squared Error (RMSE): 3.754
* R² Score: 0.313

## Testing

The project includes an automated prediction test using Pytest.

Run:

```bash
python -m pytest
```

Expected result:

```text
1 passed
```

The test checks whether the saved model can be loaded and whether the predicted grade is within the valid range of 0 to 20.

## Example

For one sample student profile, the model predicted:

```text
Predicted final grade (G3): 8.97
```

## Dataset Reference

Paulo Cortez. Student Performance. UCI Machine Learning Repository.

DOI: 10.24432/C5TG7T

## License

This project is developed for educational purposes.
