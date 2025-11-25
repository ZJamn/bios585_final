import pandas as pd
import numpy as np


def load_data(path: str) -> pd.DataFrame:
    """Load raw dataset from CSV file."""
    df = pd.read_csv(path)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning rules for BRFSS dataset:
    - Replace common missing codes (77, 88, 99, 777, 999) with NaN
    - Drop rows with any missing values
    - Ensure binary variable is integer
    """
    missing_vals = [77, 88, 99, 777, 999]
    df = df.replace(missing_vals, np.nan)

    # Drop rows containing any NA after replacement
    df = df.dropna()

    # Make sure diabetes variable is integer
    df["Diabetes_binary"] = df["Diabetes_binary"].astype(int)

    return df


def save_clean_data(df: pd.DataFrame, output_path: str):
    """Save cleaned dataset to CSV."""
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    raw_path = "../data/raw_diabetes.csv"
    out_path = "../data/cleaned_diabetes.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_data(df_raw)
    save_clean_data(df_clean, out_path)

    print("Cleaned dataset saved to:", out_path)
