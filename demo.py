from Insurance.pipeline.pipeline import Pipeline
from Insurance.exception import InsuranceException
from Insurance.logger import logging

def main():
    try:
        pipeline=Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f'{e}')
        print(e)

if __name__=="__main__":
    main()