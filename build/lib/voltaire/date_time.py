import pandas as pd

def date_time(df, date_cols):
    '''
    Function will take a data frame (df) and the name of a date column in the data frame.
    This will return the data frame (df) with month, day, and year columns (date_cols). 
    '''
    df = df.copy()
    df[date_cols] = pd.to_datetime(df[date_cols], infer_datetime_format=True)

    df[date_cols+'_month'] = df[date_cols].dt.month
    df[date_cols+'_day'] = df[date_cols].dt.day
    df[date_cols+'_year'] = df[date_cols].dt.year
    return df