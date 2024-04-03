"""
    Contains some functions to preprocess the data used in the visualisation.
"""
import pandas as pd


def convert_dates(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Converts the dates in the dataframe to datetime objects.

    Args:
        dataframe: The dataframe to process
    Returns:
        The processed dataframe with datetime-formatted dates.
    """
    # TODO : Convert dates
    dataframe["Date_Plantation"] = pd.to_datetime(dataframe["Date_Plantation"])

    return dataframe


def filter_years(dataframe, start, end):
    """
    Filters the elements of the dataframe by date, making sure
    they fall in the desired range.

    Args:
        dataframe: The dataframe to process
        start: The starting year (inclusive)
        end: The ending year (inclusive)
    Returns:
        The dataframe filtered by date.
    """
    # TODO : Filter by dates
    start = pd.to_datetime(str(start) + '-01-01')
    end = pd.to_datetime(str(end) + '-12-31')
    dataframe = dataframe[
        (dataframe["Date_Plantation"] >= start) & (dataframe["Date_Plantation"] <= end)
    ]
    return dataframe


def summarize_yearly_counts(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Groups the data by neighborhood and year,
    summing the number of trees planted in each neighborhood
    each year.

    Args:
        dataframe: The dataframe to process
    Returns:
        The processed dataframe with column 'Counts'
        containing the counts of planted
        trees for each neighborhood each year.
    """
    # TODO : Summarize df
    dataframe["year"] = dataframe["Date_Plantation"].dt.year

    summary = dataframe.groupby(["Arrond_Nom", "year"])["Arrond"].count()
    # print(summary)
    summary = summary.reset_index(name='count')
    # print(summary)
    return summary


def restructure_df(yearly_df: pd.DataFrame):
    """
    Restructures the dataframe into a format easier
    to be displayed as a heatmap.

    The resulting dataframe should have as index
    the names of the neighborhoods, while the columns
    should be each considered year. The values
    in each cell represent the number of trees
    planted by the given neighborhood the given year.

    Any empty cells are filled with zeros.

    Args:
        yearly_df: The dataframe to process
    Returns:
        The restructured dataframe
    """
    # TODO : Restructure df and fill empty cells with 0
    df = yearly_df.pivot(index='Arrond_Nom', columns="year", values="count").fillna(0)
    return df


def get_daily_info(dataframe: pd.DataFrame, arrond: int, year: int) -> pd.DataFrame:
    """
    From the given dataframe, gets
    the daily amount of planted trees
    in the given neighborhood and year.

    Args:
        dataframe: The dataframe to process
        arrond: The desired neighborhood
        year: The desired year
    Returns:
        The daily tree count data for that
        neighborhood and year.
    """
    # TODO : Get daily tree count data and return
    df = dataframe[(dataframe["Date_Plantation"].dt.year == year) & (dataframe["Arrond_Nom"] == arrond)]
    df = df[['Date_Plantation', 'Arrond']]

    df = df.groupby(["Date_Plantation"])["Arrond"].count().reset_index()

    dates = pd.date_range(df["Date_Plantation"].min(), df["Date_Plantation"].max(), name='Date_Plantation').to_series()
    full_df = pd.DataFrame(index=dates).join(df.set_index('Date_Plantation'), how='left').fillna(0).reset_index()

    return full_df
