import pymongo
import abc
import datetime
import json
import re
import pymongo
import numpy

class Logger:
    def __init__(self, db_name):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]
class text_linker:
    def __init__(self):
        self.transmit = "test"


    def connect(self, transmit):
        self.transmit = transmit
        return json.dumps({"transmit": self.transmit})

