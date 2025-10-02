# Import necessary libraries
import pandas as pd

# Load the dataset 
df = pd.read_csv('data/student_performance.csv')

# Convert categorical variables to binary

# School: GP = 1, MS = 0
df['school_binary'] = df['school'].map({'GP': 1, 'MS': 0})
# Sex: M = 1, F = 0
df['sex_binary'] = df['sex'].map({'M': 1, 'F': 0})
# Address: U = 1, R = 0
df['address_binary'] = df['address'].map({'U': 1, 'R': 0})
# Family size: GT3 = 1, LE3 = 0
df['famsize_binary'] = df['famsize'].map({'GT3': 1, 'LE3': 0})
# Parent's cohabitation status: T = 1, A = 0
df['Pstatus_binary'] = df['Pstatus'].map({'T': 1, 'A': 0}) 
# Extra educational support: yes = 1, no = 0
df['schoolsup_binary'] = df['schoolsup'].map({'yes': 1, 'no': 0})
# Family support: yes = 1, no = 0
df['famsup_binary'] = df['famsup'].map({'yes': 1, 'no': 0})
# Paid classes: yes = 1, no = 0
df['paid_binary'] = df['paid'].map({'yes': 1, 'no': 0})
# Extra-curricular activities: yes = 1, no = 0
df['activities_binary'] = df['activities'].map({'yes': 1, 'no': 0})
# Nursery attendance: yes = 1, no = 0
df['nursery_binary'] = df['nursery'].map({'yes': 1, 'no': 0})
# Higher education intention: yes = 1, no = 0
df['higher_binary'] = df['higher'].map({'yes': 1, 'no': 0})
# Internet access at home: yes = 1, no = 0
df['internet_binary'] = df['internet'].map({'yes': 1, 'no': 0})
# Romantic relationship: yes = 1, no = 0
df['romantic_binary'] = df['romantic'].map({'yes': 1, 'no': 0}) 

# One-hot encode non-binary categorical variables
# Drop first category to avoid multicollinearity in regression

# Mother's job: 'teacher', 'health', 'services', 'at_home', 'other'
df = pd.get_dummies(df, columns=['Mjob'], prefix='Mjob', drop_first=True, dtype=int)
# Father's job: 'teacher', 'health', 'services', 'at_home', 'other'
df = pd.get_dummies(df, columns=['Fjob'], prefix='Fjob', drop_first=True, dtype=int)
# Reason to choose school: 'home', 'reputation', 'course', 'other'
df = pd.get_dummies(df, columns=['reason'], prefix='reason', drop_first=True, dtype=int)
# Guardian: 'mother', 'father', 'other'
df = pd.get_dummies(df, columns=['guardian'], prefix='guardian', drop_first=True, dtype=int)    


# Drop original categorical columns
df = df.drop(columns=['school', 'sex', 'address', 'famsize', 'Pstatus', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic'])

# Check for missing values and ensure numeric data types of the all columns
df.info()

# Save the preprocessed dataset
df.to_csv('data/student_preprocessed.csv', index=False)