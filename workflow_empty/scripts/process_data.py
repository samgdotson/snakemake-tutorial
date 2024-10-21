import pandas as pd

if __name__ == "__main__":

    df = pd.read_csv(snakemake.input.data, 
                     usecols=['time', 'kw'],
                     parse_dates=True,
                     index_col='time')
    
    hours_per_day = 24
    days_per_month = 30
    df = df.rolling(hours_per_day*days_per_month).mean()

    df.to_csv(snakemake.output.processed_data)