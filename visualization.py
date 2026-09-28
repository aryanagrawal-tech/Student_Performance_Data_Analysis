import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/students_cleaned.csv")

# Study Hours vs Final Score
plt.figure(figsize=(8, 5))

sns.regplot(
    data=df,
    x="study_hours",
    y="final_score"
)

plt.title("Study Hours vs Final Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")

plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()