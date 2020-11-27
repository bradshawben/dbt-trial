#! /Users/bbradshaw/repos/venv-dbt/bin/python

import pandas as pd
import os
import zipfile


from sqlalchemy import create_engine
from kaggle.api.kaggle_api_extended import KaggleApi

if __name__ == '__main__':
    kaggle_api = KaggleApi()
    kaggle_api.authenticate()
    dir_data = '/Users/bbradshaw/repos/dbt-trial/data/'
    # Development postgres instance
    conn = 'postgresql://bbradshaw:pw@127.0.0.1:5432/flights'
    engine = create_engine(conn)

    kaggle_api.dataset_download_files('usdot/flight-delays', path=dir_data)

    with zipfile.ZipFile(os.path.join(dir_data, 'flight-delays.zip'), 'r') as f:
        f.extractall(dir_data)

    datasets = [
        'airlines',
        'airports',
        'flights'
    ]

    for d in datasets:
        data = pd.read_csv(os.path.join(dir_data, f'{d}.csv'))
        data.columns = [col.lower().strip() for col in data]
        data.to_sql(name=d, con=engine, if_exists='replace')

