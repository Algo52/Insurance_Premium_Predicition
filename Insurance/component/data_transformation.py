from Insurance.config.configuration import Configuartion
from Insurance.logger import logging
from Insurance.exception import InsuranceException
from Insurance.entity.artifact_entity import DataTransformationArtifact
from Insurance.entity.config_entity import DataTransformationConfig



class DataTransformation:

    def __init__(self, data_transformation_config: DataTransformationConfig,
                 data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_artifact: DataValidationArtifact
                 ):
        try:
            logging.info(f"{'>>' * 30}Data Transformation log started.{'<<' * 30} ")
            self.data_transformation_config= data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_artifact = data_validation_artifact

        except Exception as e:
            raise InsuranceException(e,sys) from e