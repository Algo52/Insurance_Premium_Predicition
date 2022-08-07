from Insurance.component import data_validation
from Insurance.config import configuration
from Insurance.pipeline.pipeline import Pipeline
from Insurance.exception import InsuranceException
from Insurance.logger import logging
from Insurance.config.configuration import Configuartion

def main():
    try:
        #pipeline=Pipeline()
        #pipeline.run_pipeline()
        data_valaidation_config= Configuartion().get_data_validation_config()
        print(data_valaidation_config)
    except Exception as e:
        logging.error(f'{e}')
        print(e)

if __name__=="__main__":
    main()