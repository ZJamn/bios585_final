import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm


def chi_square(df: pd.DataFrame, col: str):
    """Run chi-square test for association between categorical variable and diabetes."""
    contingency = pd.crosstab(df[col], df["Diabetes_binary"])
    chi2, p, _, _ = stats.chi2_contingency(contingency)
    return chi2, p


def correlation(df: pd.DataFrame, col: str):
    """Compute Pearson correlation between a numeric variable and diabetes."""
    r, p = stats.pearsonr(df[col], df["Diabetes_binary"])
    return r, p


def logistic_regression(df: pd.DataFrame, predictors: list):
    """Fit logistic regression model using statsmodels."""
    X = df[predictors]
    X = sm.add_constant(X)
    y = df["Diabetes_binary"]

    model = sm.Logit(y, X).fit(disp=False)
    return model.summary()
