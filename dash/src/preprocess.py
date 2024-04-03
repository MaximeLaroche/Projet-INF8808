"""
    Contains some functions to preprocess the data used in the visualisation.
"""
import pandas as pd


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the data to be used in the visualisation.

    :param df: The dataframe to preprocess.
    :return: The preprocessed dataframe.
    """
    df["sugarpercent"] *= 100
    df["pricepercent"] *= 100
    return df