from collections import namedtuple

### Giving Configuration of all the pipeline OR giving structure for the pipeline means it needs all this entities to difine thier components   
DataIngestionConfig=namedtuple("DataIngestionConfig",
["dataset_download_url","raw_data_dir","ingested_train_dir","ingested_test_dir"])


DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path","report_file_path","report_page_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig", [
                                                                   "transformed_train_dir",
                                                                   "transformed_test_dir",
                                                                   "preprocessed_object_file_path"])


ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["trained_model_file_path","base_accuracy","model_config_file_path"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path","time_stamp"])


ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])