# BIOS 585 Final Project  
**Author:** Jiamin Zhao  
**Project:** Diabetes Prediction Using BRFSS 2015 Data  

---

## 1. Project Structure
```
bios585_final/  
│── data/  
│   ├── raw_diabetes.csv  
│   └── cleaned_diabetes.csv  
│  
│── plots/  
│   ├── bmi_distribution.png  
│   ├── diabetes_by_gender.png  
│   ├── smoker_vs_diabetes.png  
│   ├── age_vs_diabetes.png  
│   ├── physactivity_vs_diabetes.png  
│   ├── bmi_age_scatter.png  
│   ├── correlation_heatmap.png  
│   ├── age_diabetes_rate.png  
│   └── logit_coefficients.png  
│  
│── src/  
│   ├── load_clean.py  
│   ├── analysis.py  
│   ├── visualization.py  
│   └── main.py  
│  
│── readme.txt  
│── report.docx  
```
---

## 2. How to Run the Program

### **Option 1 — Run from src folder**
```
cd src
python3 main.py
```

### **Option 2 — Run from project root**
```
python3 src/main.py
```


Both commands will run the full analysis pipeline.

---

## 3. What the Program Does

Running `main.py` will automatically:

- Load and clean the dataset  
- Perform all statistical analyses:
  - Chi-square tests  
  - Correlation analysis  
  - Logistic regression  
- Generate **9 visualizations** saved under `/plots/`
- Save the cleaned dataset under `/data/cleaned_diabetes.csv`

---

## 4. Package Requirements
The project uses:

- pandas  
- numpy  
- seaborn  
- matplotlib  
- statsmodels  

All are available in common Python scientific environments.

---

## 5. Notes
- Code is modularized for clarity.
- Figures and cleaned data are automatically generated.
- The project is fully reproducible by running a single script.

