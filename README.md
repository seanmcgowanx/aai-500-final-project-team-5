# Final Project - Team 5

## Project Overview


## Team Members
- Sean McGowan
- Hyunju Yu
- Deepika Shrestha

## Project Structure

`final-project-team-5/`<br>
│<br>
├─ `data/                 # Raw and processed datasets`<br>
├─ `notebooks/            # Jupyter notebooks for analysis`<br>
├─ `src/                  # Python scripts / modules`<br>
├─ `results/              # Generated plots, tables, outputs`<br>
├─ `environment.yml       # Conda environment file`<br>
└─ `README.md             # Project description and instructions`

## Setup Instructions

1. **Clone the repository**
```sh
# bash

git clone https://github.com/seanmcgowanx/aai-500-final-project-team-5.git
cd aai-500-final-project-team-5
```
2. **Create and activate the Conda environment**
```sh
# bash

conda env create -f environment.yml
conda activate final-project-team-5
```
3. **Launch JupyterLab**
```sh
#bash

jupyter lab
```
## Usage

- Notebooks in the `notebooks/` folder contain step-by-step analysis
- Python scripts in the `src/` folder can be imported for reproducible analysis
- Results (plots, tables) are saved in the `results/` folder

## Libraries Used

- `numpy` - numerical operations
- `pandas` - data manipulation
- `scipy` - statistical functions
- `matplotlib` & `seaborn` - plotting
- `scikit-learn` - modeling
- `statsmodels` - advanced statistical analysis
