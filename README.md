# Student Performance Prediction

## Project Overview

This project predicts a student's final academic grade using student-related information such as study time, previous failures, family support, absences, and other demographic and social factors.

The project uses the UCI Student Performance dataset and a Random Forest Regression model.

## Dataset

The dataset contains information about students and their academic performance.

The target variable is:

- `G3` - Final grade

The model does not use `G1` and `G2` as input features because they are earlier grades and are strongly related to the final grade.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib

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
├── .gitignore
├── README.md
└── requirements.txt

## Installation

Create and activate a virtual environment.

python3 -m venv venv

source venv/bin/activate

Install the required libraries.

pip install -r requirements.txt

## Data Preprocessing

Run:

python src/data_preprocessing.py

## Train the Model

Run:

python src/train_model.py

The trained model is saved as:

models/student_performance_model.joblib

## Make a Prediction

Run:

python src/predict.py

The program asks for student information through the command line and predicts the student's final grade.

## Model Evaluation

The current model produced:

- Mean Absolute Error (MAE): 2.966
- Root Mean Squared Error (RMSE): 3.754
- R² Score: 0.313

## Example

For one sample student profile, the model predicted:

Predicted final grade (G3): 8.97

## Dataset Reference

Paulo Cortez. Student Performance. UCI Machine Learning Repository.

DOI: 10.24432/C5TG7T

## License

This project is developed for educational purposes.