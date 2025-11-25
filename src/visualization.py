import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# 1. BMI Distribution
def plot_bmi_distribution(df):
    plt.figure(figsize=(7, 5))
    sns.histplot(df["BMI"], kde=True, bins=40)
    plt.title("BMI Distribution")
    plt.xlabel("BMI")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("../plots/bmi_distribution.png")
    plt.close()


# 2. Diabetes Rate by Gender (Sex)
def plot_diabetes_by_gender(df):
    plt.figure(figsize=(6, 5))
    gender_rate = df.groupby("Sex")["Diabetes_binary"].mean()
    gender_rate.plot(kind="bar")
    plt.title("Diabetes Rate by Gender")
    plt.ylabel("Proportion with Diabetes")
    plt.xlabel("Sex (0=Female, 1=Male)")
    plt.tight_layout()
    plt.savefig("../plots/diabetes_by_gender.png")
    plt.close()


# 3. Diabetes Rate by Smoker Status
def plot_smoker_vs_diabetes(df):
    plt.figure(figsize=(6, 5))
    smoker_rate = df.groupby("Smoker")["Diabetes_binary"].mean()
    smoker_rate.plot(kind="bar")
    plt.title("Diabetes Rate by Smoking Status")
    plt.ylabel("Proportion with Diabetes")
    plt.xlabel("Smoker (0=No, 1=Yes)")
    plt.tight_layout()
    plt.savefig("../plots/smoker_vs_diabetes.png")
    plt.close()


# 4. Age vs Diabetes (Boxplot)
def plot_age_vs_diabetes(df):
    plt.figure(figsize=(7, 5))
    sns.boxplot(x="Diabetes_binary", y="Age", data=df)
    plt.title("Age Distribution by Diabetes Status")
    plt.xlabel("Diabetes (0=No, 1=Yes)")
    plt.ylabel("Age")
    plt.tight_layout()
    plt.savefig("../plots/age_vs_diabetes.png")
    plt.close()


# 5. Physical Activity vs Diabetes
def plot_physactivity_vs_diabetes(df):
    plt.figure(figsize=(6, 5))
    pa_rate = df.groupby("PhysActivity")["Diabetes_binary"].mean()
    pa_rate.plot(kind="bar")
    plt.title("Diabetes Rate by Physical Activity Status")
    plt.ylabel("Proportion with Diabetes")
    plt.xlabel("Physical Activity (0=No, 1=Yes)")
    plt.tight_layout()
    plt.savefig("../plots/physactivity_vs_diabetes.png")
    plt.close()


# 6. Scatter: BMI vs Age colored by Diabetes
def plot_bmi_age_scatter(df):
    plt.figure(figsize=(7, 5))
    sns.scatterplot(
        x="BMI",
        y="Age",
        hue="Diabetes_binary",
        data=df,
        alpha=0.3,
        palette="coolwarm"
    )
    plt.title("BMI vs Age Colored by Diabetes Status")
    plt.tight_layout()
    plt.savefig("../plots/bmi_age_scatter.png")
    plt.close()


# 7. Correlation Heatmap (Bonus)
def plot_correlation_heatmap(df):
    plt.figure(figsize=(10, 8))
    numeric_df = df[["BMI", "Age", "Sex", "Smoker", "PhysActivity", "HighBP", "HighChol", "GenHlth", "Diabetes_binary"]]
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap of Key Variables")
    plt.tight_layout()
    plt.savefig("../plots/correlation_heatmap.png")
    plt.close()
