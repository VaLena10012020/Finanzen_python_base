from Utils.MongoClasses import MongoConnect
from datetime import datetime


class MongoLogger:
    def __init__(self, collection, logging_active):
        self.logging_active = logging_active
        self.MongoLog = MongoConnect(db='VaLenaLogging', collect=collection)
        self.APP_NAME = collection
    
    def write_log(self, logger):
        logging = {"APP": self.APP_NAME, "Message": logger, "Datetime": datetime.now()}
        if self.logging_active:
            self.MongoLog.insert_dict(logging)
        else:
            print(logging)
    
    def write_start_log(self):
        self.write_log(logger="Start service")
    
    def shut_down_log(self, logger):
        self.write_log(logger="Shutdown service")
