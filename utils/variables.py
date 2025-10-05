# --- Identify variable types ---

# Binary Categorical variables (0/1)
bin_vars = ['sex_binary', 'schoolsup_binary', 'famsup_binary', 'paid_binary', 'activities_binary', 'nursery_binary', 
'higher_binary', 'internet_binary', 'romantic_binary', ]
# Ordinal Categorical variables (1-5 scale)
ord_vars = ['Medu', 'Fedu', 'traveltime', 'studytime', 'failures', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health']
# Continuous Numeric variables
cont_vars = ['age', 'absences', 'G1', 'G2', 'G3']
# Categorical variables (including binary and ordinal)
cat_vars = bin_vars + ord_vars
# Numeric variables (including continuous and ordinal)
numeric_vars = cont_vars + ord_vars
# All variables
all_vars = cat_vars + cont_vars