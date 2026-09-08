# Student Performance Prediction

## Problem Statement

Students' final academic performance can be influenced by several factors such as study time, previous failures, family support, absences, and social or demographic conditions. It can be difficult to identify these factors and estimate a student's final grade manually.

This project uses machine learning to predict a student's final grade (`G3`) from student-related information. The project uses the UCI Student Performance dataset and a Random Forest Regression model.

## Scope of the Project

The project focuses on predicting the final grade of a student using available demographic, social, family, and study-related information.

The project includes:

* Data loading and preprocessing
* Categorical feature encoding
* Training a machine learning regression model
* Model evaluation using MAE, RMSE, and R²
* Command-line prediction for a new student profile
* Basic prediction testing

The project does not include student login management, database storage, or a web/mobile interface.

## Target Users

The intended users of this project are:

* Students interested in understanding factors related to academic performance
* Teachers or educators who want to explore student performance patterns
* Learners studying basic machine learning and regression techniques

## High-Level Features

1. **Data Preprocessing**

   * Loads the student performance dataset
   * Separates input features and the target grade
   * Encodes categorical features

2. **Model Training and Evaluation**

   * Splits the dataset into training and testing sets
   * Trains a Random Forest Regression model
   * Calculates MAE, RMSE, and R² scores
   * Saves the trained model

3. **Student Grade Prediction**

   * Accepts student information through the command line
   * Validates user inputs
   * Loads the trained model
   * Predicts the student's final grade on a 0–20 scale
