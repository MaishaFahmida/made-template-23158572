import pandas as pd
from sqlalchemy import create_engine


class Pipeline:
    def __init__(self):
        self.engine = create_engine('sqlite:///../data/Final_Data.db')
        print(self.engine)

    def get_data(self):
        url = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/precipitation_total/historical/01001_195101_202112.txt"
        # downloaded = requests.get(url)
        df = pd.read_csv(url, sep=";")
        self.data = df
        self.data.to_sql("precipitation", self.engine, index=False, if_exists='replace')
        
        
        
    def get_data1(self):
        url = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_mean/historical/01001_192201_202112.txt"
        df = pd.read_csv(url, sep=";")
        self.data2 = df
        self.data2.to_sql("Air_Temperature", self.engine, index=False, if_exists='replace')
        #print(df)
 

    def save(self):
        self.data.to_sql("Precipitation.csv", con=self.engine, index=False, if_exists='replace')

    def run_pipeline(self):
        self.get_data()
        self.get_data1()
        #self.transform()
        #self.save()


pipe = Pipeline()
pipe.run_pipeline()