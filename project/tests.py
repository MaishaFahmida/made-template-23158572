import unittest
import os
import pandas as pd
from sqlalchemy import create_engine
from pipeline import Pipeline

class TestPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the test database
        cls.engine = create_engine('sqlite:///../data/Test_Data.db')
        cls.pipeline = Pipeline()
        cls.pipeline.engine = cls.engine

    def test_get_data(self):
        # Run the pipeline's get_data method
        self.pipeline.get_data()
        # Check if the precipitation table is created and has data
        result = pd.read_sql("SELECT * FROM precipitation", self.engine)
        self.assertFalse(result.empty, "Precipitation table should not be empty")

    def test_get_data1(self):
        # Run the pipeline's get_data1 method
        self.pipeline.get_data1()
        # Check if the air temperature table is created and has data
        result = pd.read_sql("SELECT * FROM Air_Temperature", self.engine)
        self.assertFalse(result.empty, "Air_Temperature table should not be empty")

    def test_get_data3(self):
        # Ensure the prerequisite data is present
        self.pipeline.get_data1()
        # Run the pipeline's get_data3 method
        self.pipeline.get_data3()
        # Check if the transformed air temperature table is created and has data
        result = pd.read_sql("SELECT * FROM Transformed_Air_Temperature", self.engine)
        self.assertFalse(result.empty, "Transformed_Air_Temperature table should not be empty")

    @classmethod
    def tearDownClass(cls):
        # Dispose the engine to close all connections
        cls.engine.dispose()
        # Clean up the test database
        os.remove('../data/Test_Data.db')

if __name__ == '__main__':
    unittest.main()
