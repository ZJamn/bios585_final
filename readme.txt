BIOS 585 Final Project

Author: Jiamin Zhao
Project: Diabetes Prediction Using BRFSS 2015 Data

1. Project Structure
bios585_final/
│── data/
│     ├── raw_diabetes.csv
│     └── cleaned_diabetes.csv
│── plots/
│── src/
│     ├── load_clean.py
│     ├── analysis.py
│     ├── visualization.py
│     └── main.py
│── readme.txt
│── report.docx

2. How to Run the Program
Step 1 — Navigate to src folder
cd src

Step 2 — Run the full analysis pipeline
python main.py


This will:

Load and clean the dataset

Perform all statistical analyses

Generate 7 plots under /plots

Save cleaned dataset under /data

3. Files Description
load_clean.py

Reads raw dataset, replaces missing codes, drops incomplete rows, and saves cleaned CSV.

analysis.py

Contains statistical tests:

Chi-square tests

Pearson correlation

Logistic regression model

visualization.py

Generates all plots, including:

BMI distribution

Diabetes by gender

Smoker vs diabetes

Physical activity vs diabetes

Age vs diabetes

BMI–Age scatter

Correlation heatmap

main.py

Coordinates entire workflow and prints test results.

4. Analytical Research Questions

Is smoking associated with diabetes?

Is age correlated with diabetes?

Do BMI and age jointly predict diabetes?

Does diabetes prevalence differ between males and females?

Is physical activity associated with diabetes?

5. Python Packages Used

pandas

numpy

seaborn

matplotlib

scipy

statsmodels

6. Output

cleaned dataset → /data/cleaned_diabetes.csv

plots → /plots/*.png

statistical results printed in terminal