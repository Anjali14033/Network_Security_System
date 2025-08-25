import os #used for interacting with the operating system (e.g., getting environment variables, current directory, file paths).
import sys #gives access to system-specific parameters (often useful for error handling or path changes).
import json

#import the function load_dotenv from the python-dotenv library.
#This function loads environment variables from a .env file into your system environment variables so Python can access them.
from dotenv import load_dotenv 

#os.getcwd() returns the current working directory where Python is running.
# This helps check whether your .env file is inside the right folder (because load_dotenv() looks in the current directory by default).
print("Current Working Dir:", os.getcwd())

#This loads the environment variables from the .env file
load_dotenv()


print("MONGODB_URL:", os.getenv("MONGODB_URL"))

#Conclusion of this above code:- We loaded environment variables from the `.env` file and printed the MongoDB connection string (`MONGODB_URL`) from it. 

# HERE WE ARE CREATING ETL PIPELINE CODE

#Certifi is a python libraries that needs to make a secure HTTP connection
import certifi #mongoDB trust only this certificate is verified by authorities
#Certificate Authorities. This is done for SSL and TLS connections to verify that server we are connecting to has a trusted certificate ensured.
ca = certifi.where() #returns the path to the certificate file


import pandas as pd #pandas is a library used for data manipulation and analysis. It provides data structures like DataFrames to work with tabular data.
import numpy as np #numpy is a library for numerical computing in Python. It provides support for arrays, matrices, and mathematical functions to perform operations on them.
import pymongo #pymongo is a library for interacting with MongoDB from Python.
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.loggerfile import logging

# This class is responsible for extracting network data
class NetworkDataExtract:

    # Constructor for NetworkDataExtract
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    # Create a function that can convert a CSV file to JSON format
    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path) #reads the CSV file located at file_path into a pandas DataFrame.
            data.reset_index(drop=True, inplace=True) #resets the index of the DataFrame, dropping the old index and modifying the DataFrame in place.
            records = list(json.loads(data.T.to_json()).values())# converts the DataFrame to a JSON format and then loads it into a list of dictionaries, where each dictionary represents a row in the DataFrame.
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            self.records = records
            self.collection = collection
            self.database = database

            # ✅ Fetch actual URL from .env
            mongo_url = os.getenv("MONGODB_URL")

            self.mongo_client = pymongo.MongoClient(mongo_url, tlsCAFile=ca)# creates a MongoDB client using the connection string stored in the MONGODB_URL environment variable.
            self.database = self.mongo_client[self.database] #accesses the specified database within the MongoDB client.
            self.collection = self.database[self.collection] #accesses the specified collection within the database.
            self.collection.insert_many(self.records) #inserts the list of records (dictionaries) into the specified MongoDB collection.
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == "__main__":

    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "CYBERAI"
    Collection = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, Collection)
    print(no_of_records)