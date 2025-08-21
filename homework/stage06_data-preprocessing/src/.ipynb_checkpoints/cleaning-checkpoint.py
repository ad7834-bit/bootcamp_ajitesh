import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def fill_missing_median(df, columns=None):
    df_copy = df.copy()
    cols = columns if columns else df_copy.select_dtypes(include="number").columns
    for col in cols:
        median_val = df_copy[col].median()
        df_copy[col] = df_copy[col].fillna(median_val)
    return df_copy

def drop_missing(df, threshold=0.5):
    df_copy = df.copy()
    return df_copy.dropna(thresh=int(threshold * len(df_copy)))

def normalize_data(df, columns=None):
    df_copy = df.copy()
    cols = columns if columns else df_copy.select_dtypes(include="number").columns
    scaler = MinMaxScaler()
    df_copy[cols] = scaler.fit_transform(df_copy[cols])
    return df_copy
