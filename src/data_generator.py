import numpy as np
import pandas as pd

np.random.seed(42)

N = 1500  # number of samples

data = {
    "work_hours_per_day": np.random.normal(8, 2, N).clip(4, 14),
    "sleep_hours": np.random.normal(7, 1.5, N).clip(3, 9),
    "stress_level": np.random.randint(1, 11, N),
    "exercise_days_per_week": np.random.randint(0, 8, N),
    "screen_time_hours": np.random.normal(6, 2, N).clip(2, 12),
    "caffeine_intake": np.random.randint(0, 6, N),
    "mood_score": np.random.randint(1, 11, N)
}

df = pd.DataFrame(data)

# Burnout scoring logic
burnout_score = (
    (df["sleep_hours"] < 6).astype(int) * 2 +
    (df["stress_level"] > 7).astype(int) * 2 +
    (df["work_hours_per_day"] > 9).astype(int) * 2 +
    (df["exercise_days_per_week"] < 2).astype(int) +
    (df["screen_time_hours"] > 8).astype(int)
)

df["burnout_risk"] = pd.cut(
    burnout_score,
    bins=[-1, 2, 5, 10],
    labels=[0, 1, 2]
).astype(int)

# Save dataset

import os

os.makedirs("data/raw", exist_ok=True)
df.to_csv("data/raw/burnout_data.csv", index=False)

print("Dataset generated successfully!")
print(df.head())

