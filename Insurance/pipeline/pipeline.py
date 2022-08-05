from Insurance.config.configuration import Configuartion
from Insurance.logger import logging
from Insurance.exception import InsuranceException

from Insurance.entity.artifact_entity import DataIngestionArtifact
from Insurance.entity.config_entity import DataIngestionConfig
from Insurance.component.data_ingestion import DataIngestion




import os,sys

class Pipeline:

    def __init__(self,config: Configuartion = Configuartion()) -> None:
        try:
            self.config=config

        except Exception as e:
            raise InsuranceException(e,sys) from e

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise InsuranceException(e,sys) from e 

    def run_pipeline(self):
        try:
            #data ingestion

            data_ingestion_artifact = self.start_data_ingestion()
            
        
        except Exception as e:
            raise InsuranceException(e,sys) from e