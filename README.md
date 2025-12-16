# Burnout-Risk-Prediction
## Step 1: Problem & Data Design

This project predicts mental burnout risk using lifestyle and behavioral data.

### Dataset
- Synthetic dataset (1500 samples)
- Generated due to lack of public labeled burnout data
- Features include sleep, stress, work hours, exercise, and screen time

### Target Variable
Burnout risk:
- 0 → Low
- 1 → Medium
- 2 → High

### Burnout Labeling Logic
Burnout scores are calculated using domain-based heuristics such as sleep deprivation, high stress, long work hours, and low exercise frequency.

### Tools Used
- Python
- Pandas
- NumPy
