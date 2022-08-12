from Insurance.pipeline.pipeline import Pipeline
from Insurance.exception import InsuranceException
from Insurance.logger import logging
from Insurance.config.configuration import Configuartion
import os
def main():
    try:

        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path=config_path))
        #pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed.")
        #data_validation_config = Configuartion().get_data_transformation_config()
        #print(data_validation_config)
        #data_traansformation_config = Configuartion().get_data_transformation_config()
        #print(data_traansformation_config)
       
    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()