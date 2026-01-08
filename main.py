# This is a sample Python script.


import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import os
import  random
from log_code import setup_logging
logger = setup_logging("main")

from data_visualze import data_visualize



class customer_rentention_prediction_system:
    def __init__(self, path):
        self.path = path
        self.df = pd.read_csv(self.path)
        random.seed(42)
        logger.info(f"Data loaded from {self.path}")
        logger.info(f"Shape: {self.df.shape}")
        logger.info(f"Columns: {list(self.df.columns)}")
        partners = ["jio","airtel","BSNL","vodafone"]
        random_values = [random.choice(partners)  for _ in range (len(self.df))]
        self.df.insert(0, 'telecom_partner', random_values)

    def visualization(self):
        logger.info("Start visualizations")
        data_visualize(self.df)  # Call plotting function directly
        logger.info("Visualizations completed successfully")

if __name__ == '__main__':
    obj = customer_rentention_prediction_system("C:\\Users\\vishn\\OneDrive\\Desktop\\PythonProject1\\WA_Fn-UseC_-Telco-Customer-Churn.csv")
    obj.visualization()



