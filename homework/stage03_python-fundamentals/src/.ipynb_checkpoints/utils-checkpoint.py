import pandas as pd

def get_summary_stats(df):
    """
    Returns basic summary statistics for numeric columns of a DataFrame.
    """
    return df.describe()