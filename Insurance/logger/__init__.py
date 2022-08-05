from distutils.log import INFO
import logging,os
from datetime import datetime
from stat import filemode


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




""" class App_Logger:
    def __init__(self):
        pass

    def log(self,file_object,log_message):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time =self.now.strftime("%H:%M:%S")
        file_object.write(str(self.date)+"/"+str(self.current_time)+"\t\t"+ log_message +"\n")
        """