from load_clean import load_data, clean_data, save_clean_data
from analysis import chi_square, correlation, logistic_regression
from visualization import (
    plot_bmi_distribution,
    plot_diabetes_by_gender,
    plot_smoker_vs_diabetes,
    plot_age_vs_diabetes,
    plot_physactivity_vs_diabetes,
    plot_bmi_age_scatter,
    plot_correlation_heatmap
)

import os


def ensure_plot_folder():
    """Make sure plots folder exists."""
    if not os.path.exists("../plots"):
        os.makedirs("../plots")


def main():
    # Step 1: Load dataset
    df_raw = load_data("../data/raw_diabetes.csv")

    # Step 2: Clean dataset
    df_clean = clean_data(df_raw)
    save_clean_data(df_clean, "../data/cleaned_diabetes.csv")

        # Step 3: Statistical analyses
    print("\n===== Chi-square Test: Smoker vs Diabetes =====")
    chi2, p = chi_square(df_clean, "Smoker")
    print(f"Chi-square = {chi2:.3f}, p = {p:.4f}")

    print("\n===== Correlation: Age vs Diabetes =====")
    r, p = correlation(df_clean, "Age")
    print(f"Correlation r = {r:.3f}, p = {p:.4f}")

    print("\n===== Logistic Regression: BMI + Age =====")
    print(logistic_regression(df_clean, ["BMI", "Age"]))

    # ========== Q4: Sex vs Diabetes ==========
    print("\n===== Chi-square Test: Sex vs Diabetes =====")
    chi2_sex, p_sex = chi_square(df_clean, "Sex")
    print(f"Chi-square = {chi2_sex:.3f}, p = {p_sex:.4f}")

    # ========== Q5: Physical Activity vs Diabetes ==========
    print("\n===== Chi-square Test: Physical Activity vs Diabetes =====")
    chi2_pa, p_pa = chi_square(df_clean, "PhysActivity")
    print(f"Chi-square = {chi2_pa:.3f}, p = {p_pa:.4f}")

    

        # Step 4: Create plots
    ensure_plot_folder()
    plot_bmi_distribution(df_clean)
    plot_diabetes_by_gender(df_clean)
    plot_smoker_vs_diabetes(df_clean)
    plot_age_vs_diabetes(df_clean)
    plot_physactivity_vs_diabetes(df_clean)
    plot_bmi_age_scatter(df_clean)
    plot_correlation_heatmap(df_clean)


    print("\nPlots saved in ../plots/")
    print("Cleaned dataset saved in ../data/cleaned_diabetes.csv")


if __name__ == "__main__":
    main()
