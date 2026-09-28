import numpy as np
import pandas as pd

# Make random data reproducible
np.random.seed(42)

# Number of students
n_students = 200

# Student IDs
student_id = np.arange(1, n_students + 1)

# Student names
names = [
    "Aarav", "Aditi", "Rahul", "Priya", "Arjun",
    "Ananya", "Rohan", "Kavya", "Vivek", "Meera",
    "Aditya", "Isha", "Karan", "Neha", "Dev",
    "Riya", "Yash", "Pooja", "Manav", "Diya"
]

name = np.random.choice(names, n_students)

# Gender
gender = np.random.choice(
    ["Male", "Female"],
    n_students
)

# Age between 18 and 22
age = np.random.randint(
    18, 23,
    n_students
)

# Average daily study hours
study_hours = np.round(
    np.random.uniform(1, 6, n_students),
    1
)

# Attendance percentage
attendance = np.round(
    np.random.uniform(50, 100, n_students),
    1
)

# Number of completed assignments
assignments_completed = np.random.randint(
    3, 11,
    n_students
)

# Midterm score
midterm_score = np.random.randint(
    40, 96,
    n_students
)

# Average daily sleep hours
sleep_hours = np.round(
    np.random.uniform(5, 9, n_students),
    1
)

# Internet access
internet_access = np.random.choice(
    ["Yes", "No"],
    n_students
)

# Extracurricular activity
extracurricular = np.random.choice(
    ["Yes", "No"],
    n_students
)

# Generate final score
final_score = (
    midterm_score * 0.35
    + study_hours * 5
    + attendance * 0.20
    + assignments_completed * 1.5
    + np.random.normal(0, 5, n_students)
)

# Keep scores between 0 and 100
final_score = np.clip(final_score, 0, 100)

# Round final scores to one decimal place
final_score = np.round(final_score, 1)

# Create Pandas DataFrame
df = pd.DataFrame({
    "student_id": student_id,
    "name": name,
    "gender": gender,
    "age": age,
    "study_hours": study_hours,
    "attendance": attendance,
    "assignments_completed": assignments_completed,
    "midterm_score": midterm_score,
    "final_score": final_score,
    "sleep_hours": sleep_hours,
    "internet_access": internet_access,
    "extracurricular": extracurricular
})

# Save dataset
df.to_csv("data/students.csv", index=False)

# Display confirmation
print("Dataset created successfully!")
print()
print("First 5 rows:")
print(df.head())

print()
print("Dataset shape:")
print(df.shape)

# Create a copy of the clean dataset
raw_df = df.copy()

# Add some missing values
raw_df.loc[5, "study_hours"] = np.nan
raw_df.loc[15, "attendance"] = np.nan
raw_df.loc[25, "midterm_score"] = np.nan

# Add invalid values
raw_df.loc[35, "attendance"] = 120
raw_df.loc[45, "study_hours"] = -2

# Add inconsistent gender values
raw_df.loc[55, "gender"] = "male"
raw_df.loc[65, "gender"] = "MALE"

# Add a duplicate row
raw_df.loc[75] = raw_df.loc[74]

# Save raw dataset
raw_df.to_csv("data/students_raw.csv", index=False)

print("Raw dataset created!")
print(raw_df.shape)