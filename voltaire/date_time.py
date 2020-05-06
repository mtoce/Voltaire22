import pandas as pd


#df = pd.read_csv('https://raw.githubusercontent.com/mtoce/Build2-Project/master/astros_bangs_20200127.csv')

class Date_time:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def date(self, df, date_cols):
        '''
        Function will take a data frame (df)
        and the name of a date column in the data frame.
        This will return the data frame (df)
        with month, day, and year columns (date_cols).
        '''
        df = df.copy()
        df[date_cols] = pd.to_datetime(df[date_cols], infer_datetime_format=True)

        df[date_cols+'_month'] = df[date_cols].dt.month
        df[date_cols+'_day'] = df[date_cols].dt.day
        df[date_cols+'_year'] = df[date_cols].dt.year
        return df

if __name__ == "__main__":
    df = pd.read_csv('https://raw.githubusercontent.com/mtoce/Build2-Project/master/astros_bangs_20200127.csv')
    date_time_test = Date_time(1, 1, 2001)
    p1 = date_time_test.date(df=df, date_cols='game_date')
    print(p1)