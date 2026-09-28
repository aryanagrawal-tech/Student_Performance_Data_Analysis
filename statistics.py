import pandas as pd
import numpy as np


# ==========================================
# LOAD CLEANED DATASET
# ==========================================

df = pd.read_csv("data/students_cleaned.csv")

print("========== DATASET ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ==========================================
# 1. FINAL SCORE STATISTICS
# ==========================================

print("\n========== FINAL SCORE STATISTICS ==========")

final_score_mean = df["final_score"].mean()
final_score_median = df["final_score"].median()
final_score_min = df["final_score"].min()
final_score_max = df["final_score"].max()
final_score_std = df["final_score"].std()

print("Mean:", round(final_score_mean, 2))
print("Median:", round(final_score_median, 2))
print("Minimum:", final_score_min)
print("Maximum:", final_score_max)
print("Standard Deviation:", round(final_score_std, 2))


# ==========================================
# 2. STUDY HOURS STATISTICS
# ==========================================

print("\n========== STUDY HOURS STATISTICS ==========")

print("Mean:",
      round(df["study_hours"].mean(), 2))

print("Median:",
      round(df["study_hours"].median(), 2))

print("Minimum:",
      df["study_hours"].min())

print("Maximum:",
      df["study_hours"].max())


# ==========================================
# 3. ATTENDANCE STATISTICS
# ==========================================

print("\n========== ATTENDANCE STATISTICS ==========")

print("Mean:",
      round(df["attendance"].mean(), 2))

print("Median:",
      round(df["attendance"].median(), 2))

print("Minimum:",
      df["attendance"].min())

print("Maximum:",
      df["attendance"].max())


# ==========================================
# 4. MIDTERM SCORE STATISTICS
# ==========================================

print("\n========== MIDTERM SCORE STATISTICS ==========")

print("Mean:",
      round(df["midterm_score"].mean(), 2))

print("Median:",
      round(df["midterm_score"].median(), 2))

print("Minimum:",
      df["midterm_score"].min())

print("Maximum:",
      df["midterm_score"].max())


# ==========================================
# 5. NUMPY STATISTICS
# ==========================================

print("\n========== NUMPY ANALYSIS ==========")

final_scores = df["final_score"].to_numpy()

print("Mean:",
      round(np.mean(final_scores), 2))

print("Median:",
      round(np.median(final_scores), 2))

print("Standard Deviation:",
      round(np.std(final_scores), 2))

print("Variance:",
      round(np.var(final_scores), 2))


# ==========================================
# 6. AVERAGE FINAL SCORE BY GENDER
# ==========================================

print("\n========== FINAL SCORE BY GENDER ==========")

gender_analysis = (
    df.groupby("gender")["final_score"]
    .agg(["mean", "median", "count"])
)

gender_analysis = gender_analysis.round(2)

print(gender_analysis)


# ==========================================
# 7. FINAL SCORE BY INTERNET ACCESS
# ==========================================

print("\n========== FINAL SCORE BY INTERNET ACCESS ==========")

internet_analysis = (
    df.groupby("internet_access")["final_score"]
    .agg(["mean", "median", "count"])
)

internet_analysis = internet_analysis.round(2)

print(internet_analysis)


# ==========================================
# 8. FINAL SCORE BY EXTRACURRICULAR ACTIVITY
# ==========================================

print("\n========== FINAL SCORE BY EXTRACURRICULAR ==========")

extra_analysis = (
    df.groupby("extracurricular")["final_score"]
    .agg(["mean", "median", "count"])
)

extra_analysis = extra_analysis.round(2)

print(extra_analysis)


# ==========================================
# 9. FINAL SCORE BY ASSIGNMENTS
# ==========================================

print("\n========== FINAL SCORE BY ASSIGNMENTS ==========")

assignment_analysis = (
    df.groupby("assignments_completed")["final_score"]
    .agg(["mean", "median", "count"])
)

assignment_analysis = assignment_analysis.round(2)

print(assignment_analysis)


# ==========================================
# 10. CORRELATION WITH FINAL SCORE
# ==========================================

print("\n========== CORRELATION WITH FINAL SCORE ==========")

correlation = (
    df.corr(numeric_only=True)["final_score"]
    .sort_values(ascending=False)
)

print(correlation.round(3))


# ==========================================
# 11. TOP 10 STUDENTS
# ==========================================

print("\n========== TOP 10 STUDENTS ==========")

top_students = (
    df.sort_values(
        by="final_score",
        ascending=False
    )
    [
        [
            "student_id",
            "name",
            "study_hours",
            "attendance",
            "midterm_score",
            "final_score"
        ]
    ]
    .head(10)
)

print(top_students.to_string(index=False))


# ==========================================
# 12. BOTTOM 10 STUDENTS
# ==========================================

print("\n========== BOTTOM 10 STUDENTS ==========")

bottom_students = (
    df.sort_values(
        by="final_score",
        ascending=True
    )
    [
        [
            "student_id",
            "name",
            "study_hours",
            "attendance",
            "midterm_score",
            "final_score"
        ]
    ]
    .head(10)
)

print(bottom_students.to_string(index=False))


# ==========================================
# 13. PERFORMANCE CATEGORIES
# ==========================================

df["performance"] = pd.cut(
    df["final_score"],
    bins=[0, 50, 60, 70, 80, 90, 100],
    labels=[
        "Poor",
        "Below Average",
        "Average",
        "Good",
        "Very Good",
        "Excellent"
    ]
)

print("\n========== PERFORMANCE CATEGORIES ==========")

performance_counts = (
    df["performance"]
    .value_counts()
    .sort_index()
)

print(performance_counts)


# ==========================================
# 14. PERFORMANCE PERCENTAGE
# ==========================================

print("\n========== PERFORMANCE PERCENTAGE ==========")

performance_percentage = (
    df["performance"]
    .value_counts(normalize=True)
    .sort_index()
    * 100
)

print(performance_percentage.round(2))


# ==========================================
# END
# ==========================================

print("\n==========================================")
print("Statistical analysis completed!")
print("==========================================")