import logging
from datetime import datetime
import os
import pandas as pd
from Insurance.constant import get_current_time_stamp 


LOG_DIR="logs"

CURRENT_TIME_STAMP=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log"



""" creating dir to store the log file"""
os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s',
level=logging.INFO
)

def get_log_dataframe(file_path):
    data=[]
    with open(file_path) as log_file:
        for line in log_file.readlines():
            data.append(line.split("^;"))

    log_df = pd.DataFrame(data)
    columns=["Time stamp","Log Level","line number","file name","function name","message"]
    log_df.columns=columns
    
    log_df["log_message"] = log_df['Time stamp'].astype(str) +":$"+ log_df["message"]

    return log_df[["log_message"]]



""" class App_Logger:
    def __init__(self):
        pass

    def log(self,file_object,log_message):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time =self.now.strftime("%H:%M:%S")
        file_object.write(str(self.date)+"/"+str(self.current_time)+"\t\t"+ log_message +"\n")
        """