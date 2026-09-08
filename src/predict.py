import pandas as pd
import joblib

# Load the trained model
model = joblib.load("models/student_performance_model.joblib")

print("Student Performance Prediction")
print("--------------------------------")


def get_choice(prompt, choices):
    while True:
        value = input(prompt).strip()
        if value in choices:
            return value
        print("Invalid input. Please choose from:", ", ".join(choices))


def get_int(prompt, minimum, maximum=None):
    while True:
        try:
            value = int(input(prompt).strip())
            if value < minimum or (maximum is not None and value > maximum):
                if maximum is None:
                    print(f"Please enter a value of {minimum} or greater.")
                else:
                    print(f"Please enter a value between {minimum} and {maximum}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


# Get student information
school = get_choice("School (GP/MS): ", ["GP", "MS"])
sex = get_choice("Sex (F/M): ", ["F", "M"])
age = get_int("Age: ", 15, 25)
address = get_choice("Address (U/R): ", ["U", "R"])
famsize = get_choice("Family size (LE3/GT3): ", ["LE3", "GT3"])
Pstatus = get_choice("Parent status (T/A): ", ["T", "A"])

Medu = get_int("Mother's education (0-4): ", 0, 4)
Fedu = get_int("Father's education (0-4): ", 0, 4)

Mjob = get_choice(
    "Mother's job (teacher/health/services/at_home/other): ",
    ["teacher", "health", "services", "at_home", "other"]
)

Fjob = get_choice(
    "Father's job (teacher/health/services/at_home/other): ",
    ["teacher", "health", "services", "at_home", "other"]
)

reason = get_choice(
    "Reason for choosing school (home/reputation/course/other): ",
    ["home", "reputation", "course", "other"]
)

guardian = get_choice(
    "Guardian (mother/father/other): ",
    ["mother", "father", "other"]
)

traveltime = get_int("Travel time (1-4): ", 1, 4)
studytime = get_int("Study time (1-4): ", 1, 4)
failures = get_int("Past class failures (0-3): ", 0, 3)

schoolsup = get_choice("School educational support (yes/no): ", ["yes", "no"])
famsup = get_choice("Family educational support (yes/no): ", ["yes", "no"])
paid = get_choice("Extra paid classes (yes/no): ", ["yes", "no"])
activities = get_choice("Extra-curricular activities (yes/no): ", ["yes", "no"])
nursery = get_choice("Attended nursery school (yes/no): ", ["yes", "no"])
higher = get_choice("Wants higher education (yes/no): ", ["yes", "no"])
internet = get_choice("Internet access at home (yes/no): ", ["yes", "no"])
romantic = get_choice("In a romantic relationship (yes/no): ", ["yes", "no"])

famrel = get_int("Family relationship quality (1-5): ", 1, 5)
freetime = get_int("Free time after school (1-5): ", 1, 5)
goout = get_int("Going out frequency (1-5): ", 1, 5)
Dalc = get_int("Workday alcohol consumption (1-5): ", 1, 5)
Walc = get_int("Weekend alcohol consumption (1-5): ", 1, 5)
health = get_int("Current health status (1-5): ", 1, 5)
absences = get_int("Number of school absences: ", 0)


# Create input DataFrame
student = pd.DataFrame([{
    "school": school,
    "sex": sex,
    "age": age,
    "address": address,
    "famsize": famsize,
    "Pstatus": Pstatus,
    "Medu": Medu,
    "Fedu": Fedu,
    "Mjob": Mjob,
    "Fjob": Fjob,
    "reason": reason,
    "guardian": guardian,
    "traveltime": traveltime,
    "studytime": studytime,
    "failures": failures,
    "schoolsup": schoolsup,
    "famsup": famsup,
    "paid": paid,
    "activities": activities,
    "nursery": nursery,
    "higher": higher,
    "internet": internet,
    "romantic": romantic,
    "famrel": famrel,
    "freetime": freetime,
    "goout": goout,
    "Dalc": Dalc,
    "Walc": Walc,
    "health": health,
    "absences": absences
}])


# Predict final grade
prediction = model.predict(student)[0]

# Keep prediction within the valid grade range
prediction = max(0, min(20, prediction))

print()
print("Predicted final grade (G3):", round(prediction, 2))
print("--------------------------------")
