import pandas as pd

def get_data_electric_production_raw():
    return pd.read_csv('data/Electric_Production.csv')

def process_data(df):
    # change date format
    df0=df.copy()
    df0['date']=pd.to_datetime(df0['DATE'],errors='coerce')
    df0['DATE']=df0.date.apply(lambda x:x.strftime('%y-%m-%d'))
    df0.drop(columns=['DATE'],inplace=True)
    # rename columns
    df0.columns=['production','prod_date']
    df1=df0[['prod_date','production']].copy()
    return df1