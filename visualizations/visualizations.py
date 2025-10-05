import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime


# Create output directory for visualizations
output_dir = os.path.dirname(__file__)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# Load the dataset
data_path = os.path.join(os.path.dirname(__file__), '../data/student_preprocessed.csv')
df = pd.read_csv(data_path)

# Display basic info about the dataset
df_info = df.info()
df_head = df.head()
df_description = df.describe(include="all")

df_head, df_description

# Set style
sns.set(style="whitegrid", palette="muted", font_scale=1.1)

# 1. Distributions & Skewness
continuous_vars = ["age", "absences", "G1", "G2", "G3"]

fig, axes = plt.subplots(len(continuous_vars), 2, figsize=(12, 18))

for i, var in enumerate(continuous_vars):
    # Histogram with KDE
    sns.histplot(df[var], kde=True, ax=axes[i, 0], color="skyblue")
    skewness = df[var].skew()
    axes[i, 0].set_title(f"Distribution of {var} (Skewness: {skewness:.2f})")
    
    # Boxplot
    sns.boxplot(x=df[var], ax=axes[i, 1], color="lightcoral")
    axes[i, 1].set_title(f"Boxplot of {var}")

plt.tight_layout()
plt.savefig(os.path.join(output_dir, f'distributions_and_skewness_{timestamp}.png'), dpi=300, bbox_inches='tight')
plt.show()
plt.close()




# 2. Correlation, Scatter plots with regression lines
# Scatter plots with regression lines for key relationships
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# G1 vs G3
sns.regplot(x="G1", y="G3", data=df, ax=axes[0, 0], scatter_kws={'alpha':0.5}, line_kws={"color":"red"})
axes[0, 0].set_title("Regression: G1 vs Final Grade (G3)")

# G2 vs G3
sns.regplot(x="G2", y="G3", data=df, ax=axes[0, 1], scatter_kws={'alpha':0.5}, line_kws={"color":"red"})
axes[0, 1].set_title("Regression: G2 vs Final Grade (G3)")

# Studytime vs G3
sns.regplot(x="studytime", y="G3", data=df, ax=axes[1, 0], scatter_kws={'alpha':0.6}, line_kws={"color":"red"})
axes[1, 0].set_title("Regression: Study Time vs Final Grade (G3)")

# Failures vs G3
sns.regplot(x="failures", y="G3", data=df, ax=axes[1, 1], scatter_kws={'alpha':0.6}, line_kws={"color":"red"})
axes[1, 1].set_title("Regression: Past Failures vs Final Grade (G3)")

plt.tight_layout()
plt.savefig(os.path.join(output_dir, f'regression_analysis_{timestamp}.png'), dpi=300, bbox_inches='tight')
plt.show()
plt.close()


# 3. Group Comparisons (Boxplots & Bar charts)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Boxplot: G3 by sex
sns.boxplot(x="sex_binary", y="G3", data=df, ax=axes[0, 0])
axes[0, 0].set_title("Final Grade (G3) by Sex (0=Male, 1=Female)")

# Boxplot: G3 by school
sns.boxplot(x="school_binary", y="G3", data=df, ax=axes[0, 1])
axes[0, 1].set_title("Final Grade (G3) by School (0=MS, 1=GP)")

# Barplot: Mother education vs. mean G3
sns.barplot(x="Medu", y="G3", data=df, ci=None, ax=axes[1, 0])
axes[1, 0].set_title("Mother Education Level vs. Mean Final Grade (G3)")

# Barplot: Father education vs. mean G3
sns.barplot(x="Fedu", y="G3", data=df, ci=None, ax=axes[1, 1])
axes[1, 1].set_title("Father Education Level vs. Mean Final Grade (G3)")

plt.tight_layout()
plt.savefig(os.path.join(output_dir, f'group_comparisons_{timestamp}.png'), dpi=300, bbox_inches='tight')
plt.show()
plt.close()