from Insurance.entity.config_entity import DataIngestionConfig
import sys,os
from Insurance.exception import InsuranceException
from Insurance.logger import logging
from Insurance.entity.artifact_entity import DataIngestionArtifact
import tarfile
import numpy as np
from six.moves import urllib
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig ):
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20} ")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise InsuranceException(e,sys) from e
    

    def download_housing_data(self,) -> str:
        try:
            #raise Exception("heamdjsadhs")
            #extraction remote url to download dataset
            download_url = self.data_ingestion_config.dataset_download_url

            #folder location to download file
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir,exist_ok=True)

            insurance_file_name = os.path.basename(download_url)

            raw_file_path = os.path.join(raw_data_dir, insurance_file_name)

            logging.info(f"Downloading file from :[{download_url}] into :[{raw_file_path}]")
            urllib.request.urlretrieve(download_url, raw_file_path)
            logging.info(f"File :[{raw_file_path}] has been downloaded successfully.")
            return raw_file_path

        except Exception as e:
            raise InsuranceException(e,sys) from e

    
    
    def split_data_as_train_test(self) -> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            file_name = os.listdir(raw_data_dir)[0]

            insurance_file_path = os.path.join(raw_data_dir,file_name)


            logging.info(f"Reading csv file: [{insurance_file_path}]")
            insurance_data_frame = pd.read_csv(insurance_file_path)

            insurance_data_frame["expense_cat"] = pd.cut(
                insurance_data_frame["expenses"],
                bins=[1000, 10000, 20000, 30000, 40000, np.inf],
                labels=[1,2,3,4,5]
            )
            

            logging.info(f"Splitting data into train and test")
            strat_train_set = None
            strat_test_set = None

            split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

            for train_index,test_index in split.split(insurance_data_frame, insurance_data_frame["expense_cat"]):
                strat_train_set = insurance_data_frame.loc[train_index].drop(["expense_cat"],axis=1)
                strat_test_set = insurance_data_frame.loc[test_index].drop(["expense_cat"],axis=1)

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,
                                            file_name)

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,
                                        file_name)
            
            if strat_train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
                logging.info(f"Exporting training datset to file: [{train_file_path}]")
                strat_train_set.to_csv(train_file_path,index=False)

            if strat_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok= True)
                logging.info(f"Exporting test dataset to file: [{test_file_path}]")
                strat_test_set.to_csv(test_file_path,index=False)
            

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                test_file_path=test_file_path,
                                is_ingested=True,
                                message=f"Data ingestion completed successfully."
                                )
            logging.info(f"Data Ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact

        except Exception as e:
            raise InsuranceException(e,sys) from e

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            raw_file_path =  self.download_housing_data()
            return self.split_data_as_train_test()
        except Exception as e:
            raise InsuranceException(e,sys) from e
    


    def __del__(self):
        logging.info(f"{'='*20}Data Ingestion log completed.{'='*20} \n\n")