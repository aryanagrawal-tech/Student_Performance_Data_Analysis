import pandas as pd


# ==========================================
# LOAD RAW DATASET
# ==========================================

df = pd.read_csv("data/students_raw.csv")

print("========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== COLUMN NAMES ==========")
print(df.columns)

print("\n========== DATA TYPES ==========")
df.info()

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())


# ==========================================
# DATA CLEANING
# ==========================================

# Make a copy so the raw data remains unchanged
clean_df = df.copy()


# ------------------------------------------
# 1. STANDARDIZE GENDER VALUES
# ------------------------------------------

clean_df["gender"] = (
    clean_df["gender"]
    .str.strip()
    .str.title()
)


# ------------------------------------------
# 2. HANDLE INVALID ATTENDANCE
# ------------------------------------------

clean_df.loc[
    (clean_df["attendance"] < 0) |
    (clean_df["attendance"] > 100),
    "attendance"
] = pd.NA


# ------------------------------------------
# 3. HANDLE INVALID STUDY HOURS
# ------------------------------------------

clean_df.loc[
    clean_df["study_hours"] < 0,
    "study_hours"
] = pd.NA


# ------------------------------------------
# 4. REMOVE DUPLICATE ROWS
# ------------------------------------------

clean_df = clean_df.drop_duplicates()


# ------------------------------------------
# 5. FILL MISSING VALUES
# ------------------------------------------

clean_df["study_hours"] = clean_df["study_hours"].fillna(
    clean_df["study_hours"].median()
)

clean_df["attendance"] = clean_df["attendance"].fillna(
    clean_df["attendance"].median()
)

clean_df["midterm_score"] = clean_df["midterm_score"].fillna(
    clean_df["midterm_score"].median()
)


# ==========================================
# CHECK CLEANING RESULTS
# ==========================================

print("\n========== AFTER CLEANING ==========")

print("\nMissing values:")
print(clean_df.isnull().sum())

print("\nDuplicate rows:")
print(clean_df.duplicated().sum())

print("\nGender values:")
print(clean_df["gender"].value_counts())

print("\nCleaned shape:")
print(clean_df.shape)


# ==========================================
# SAVE CLEANED DATASET
# ==========================================

clean_df.to_csv(
    "data/students_cleaned.csv",
    index=False
)

print("\n==========================================")
print("Cleaned dataset saved successfully!")
print("File: data/students_cleaned.csv")
print("==========================================")