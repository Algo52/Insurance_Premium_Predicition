from Insurance.entity.artifact_entity import DataValidationArtifact
from Insurance.entity.config_entity import DataValidationConfig
from Insurance.exception import InsuranceException
from Insurance.logger import logging
import sys,os
class DataValidation:
    

    def __init__(self, data_validation_config:DataValidationConfig,
        data_ingestion_artifact:DataIngestionArtifact):
        try:
            pass
        except Exception as e:
            raise InsuranceException(e,sys) from e