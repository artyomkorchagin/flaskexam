import json
import pymongo


class Logger:
    def __init__(self, db_name):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]

class Govno:
    def __init__(self):
        self.n_1 = 'test1'
        self.n_2 = 'test2'
        print(self.n_1, self.n_2)

    def connect(self, request):
        self.n_1 = request.args.get('id1')
        self.n_2 = request.args.get('id2')
        return print("done")

    def get_value(self):
        return json.dumps({'n_1': self.n_1, 'n_2': self.n_2})


