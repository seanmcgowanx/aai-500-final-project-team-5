import pandas as pd
from scipy import stats
import os
from scipy.stats import chi2_contingency

# Load data
data_path = os.path.join(os.path.dirname(__file__), '../data/student_preprocessed.csv')
df = pd.read_csv(data_path)

# Separate groups
female = df[df["sex"] == 0]["G3"]
male = df[df["sex"] == 1]["G3"]

# Welch’s t-test (unequal variances)
t_stat, p_val = stats.ttest_ind(male, female, equal_var=False)

print("=== T-test: G3 by Gender (0=Female, 1=Male) ===")
print(f"t-statistic = {t_stat:.3f}")
print(f"p-value = {p_val:.4f}")

if p_val < 0.05:
    print("Reject H₀: There is a significant difference in mean G3 between male and female students.")
else:
    print("Fail to reject H₀: No signiclficant difference in mean G3 between male and female students.")


# T-test: mean grade difference by school
# Separate students by school
gp = df[df["school"] == 1]["G3"]
ms = df[df["school"] == 0]["G3"]

# Perform Welch’s t-test (unequal variances)
t_stat, p_val = stats.ttest_ind(gp, ms, equal_var=False)

print("=== T-test: G3 by School (GP vs MS) ===")
print(f"t-statistic = {t_stat:.3f}")
print(f"p-value = {p_val:.4f}")

# Interpretation
if p_val < 0.05:
    print("Reject H₀: There is a significant difference in mean G3 between the two schools.")
else:
    print("Fail to reject H₀: No significant difference in mean G3 between the two schools.")

# Chi-Squared Test of Independence for Categorical Variables
# Define categorical variable pairs to test
chi_pairs = [
    ('sex', 'higher'),
    ('romantic', 'higher')
]


# Run Chi-square tests
results = []

for var1, var2 in chi_pairs:
    contingency = pd.crosstab(df[var1], df[var2])
    chi2, p, dof, expected = chi2_contingency(contingency)
    n = contingency.sum().sum()
    
    results.append({
        'Variable 1': var1,
        'Variable 2': var2,
        'Chi2': round(chi2, 4),
        'p-value': round(p, 6),
    })

# Convert results to DataFrame
chi_results = pd.DataFrame(results)
print("\nChi-Square Test Results:\n")
print(chi_results)
