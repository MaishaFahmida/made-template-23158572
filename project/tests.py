import unittest
import os, requests
import pandas as pd
from sqlalchemy import create_engine
from pipeline import Pipeline

class TestPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
    
        cls.engine = create_engine('sqlite:///../data/Test_Data.db')
        cls.pipeline = Pipeline()
        cls.pipeline.engine = cls.engine

    def test_get_data(self):
        
        self.pipeline.get_data()
        
        result = pd.read_sql("SELECT * FROM precipitation", self.engine)
        self.assertFalse(result.empty, "Precipitation table should not be empty")

    def test_get_data1(self):
        
        self.pipeline.get_data1()
        
        result = pd.read_sql("SELECT * FROM Air_Temperature", self.engine)
        self.assertFalse(result.empty, "Air_Temperature table should not be empty")

    def test_get_data3(self):
        
        self.pipeline.get_data1()
        
        self.pipeline.get_data3()
        
        result = pd.read_sql("SELECT * FROM Transformed_Air_Temperature", self.engine)
        self.assertFalse(result.empty, "Transformed_Air_Temperature table should not be empty")

    @classmethod
    def tearDownClass(cls):
        
        cls.engine.dispose()
        
        os.remove('../data/Test_Data.db')

if __name__ == '__main__':
    unittest.main()
