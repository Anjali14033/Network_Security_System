from networksecurity.exception.exception import NetworkSecurityException # here we return custom exception
from networksecurity.logging.loggerfile import logging

##configuration of the Data Ingestion Config

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact
import os
import sys
import numpy as np
import pandas as pd
import pymongo
from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGODB_URL")


class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def export_collection_as_dataframe(self):
        """Read Data from MongoDB Collection and convert to DataFrame
        """
        try:
            Database_Name = self.data_ingestion_config.database_name
            Collection_Name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongo_client[Database_Name][Collection_Name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            df.replace({"na": np.NAN}, inplace=True)
            return df
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def export_data_to_feature_store(self, dataframe: pd.DataFrame):
        """Export the processed DataFrame to a feature store
        """
        try:
            # Code to export dataframe to feature store
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            #creating folder
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        """Split the data into train and test set
        """
        try:
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_file_ratio
            )
            logging.info("Performed train test split on the dataframe")

            logging.info("Exited split_data_as_train_test method on Data_Ingested class")

            #save the train and test file to the local file system
            train_file_path = self.data_ingestion_config.training_file_path
            test_file_path = self.data_ingestion_config.testing_file_path

            #creating folder
            dir_path = os.path.dirname(train_file_path)
            os.makedirs(dir_path, exist_ok=True)

            logging.info(f"Exporting train and test file path.")

            train_set.to_csv(train_file_path, index=False, header=True)
            test_set.to_csv(test_file_path, index=False, header=True)

            logging.info(f"Exported train and test file path.")
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def initiate_data_ingestion(self):

        """Initiate the data ingestion process 
        """
        try:
            dataframe = self.export_collection_as_dataframe()
            dataframe = self.export_data_to_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            data_ingestion_artifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path)
            return data_ingestion_artifact
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
