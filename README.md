# Predicting Student Performance in Portuguese Secondary Schools

## Study Overview

Dataset: "Student Performance" dataset by Paulo Cortez and Alice M. G. Silva (UCI Machine Learning Repository, 2008).

This study aimed to develop and compare predictive models for student final grades (G3) using academic, behavioral, and demographic variables. The analysis evaluated linear and ensemble algorithms to identify both the most accurate predictive framework and the key factors, including early-term grades and secondary predictors, that influence student performance.

## Team Members
- Sean McGowan
- Hyunju Yu
- Deepika Shrestha

## Project Structure

`student-performance/`<br>
│<br>
├─ `data/                 # Raw and processed datasets`<br>
├─ `notebooks/            # Jupyter notebooks for analysis`<br>
├─ `visualizations/       # Saved figures from the notebook`<br>
├─ `environment.yml       # Conda environment file`<br>
└─ `README.md             # Project description and instructions`

## Setup Instructions

1. **Clone the repository** 
```sh
git clone https://github.com/seanmcgowanx/student-performance.git
cd student-performance
```
2. **Create the Conda environment** 
```sh
conda env create -f environment.yml
```
3. **Activate the Conda environment** 
```sh
conda activate final-project-team-5
``` 
## Usage

- Notebooks in the `notebooks/` folder contain step-by-step analysis


## Libraries Used

- `numpy` - numerical operations
- `pandas` - data manipulation
- `scipy` - statistical functions
- `matplotlib` & `seaborn` - plotting
- `scikit-learn` - modeling
- `statsmodels` - advanced statistical analysis
