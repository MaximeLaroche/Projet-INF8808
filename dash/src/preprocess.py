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
    print(df.columns)

    df = df.astype(
        {
            "competitorname": str,
            "chocolate": bool,
            "fruity": bool,
            "caramel": bool,
            "peanutyalmondy": bool,
            "nougat": bool,
            "crispedricewafer": bool,
            "hard": bool,
            "bar": bool,
            "pluribus": bool,
            "sugarpercent": int,
            "pricepercent": int,
            "winpercent": int,
        }
    )
    print(df.head())
    print(df.dtypes)
    return df
