# --- Identify variable types ---

# Binary Categorical variables (0/1)
bin_vars = ['school', 'sex', 'address', 'famsize', 'Pstatus', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 
'higher', 'internet', 'romantic']
# Ordinal Categorical variables (1-5 scale)
ord_vars = ['Medu', 'Fedu', 'traveltime', 'studytime', 'failures', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health']
# Nominal Categorical variables (more than 2 categories)
nom_vars = ['Mjob', 'Fjob', 'reason', 'guardian']
# Continuous Numeric variables
cont_vars = ['age', 'absences', 'G1', 'G2', 'G3']
# Categorical variables (including binary and ordinal)
cat_vars = bin_vars + ord_vars + nom_vars
# Numeric variables (including continuous and ordinal)
numeric_vars = cont_vars + ord_vars
# All variables
all_vars = cat_vars + cont_vars