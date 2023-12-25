import json
import pymongo
import datetime


class Logger:
    def __init__(self, db_name):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]
        self.current_govno = []

    def insert_govno(self, new_data, collection):
        if new_data == self.current_govno:
            print('Value has not changed')
        else:
            self.current_govno = new_data
            return self.db[collection].insert_one({
                'Timestep': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                collection: new_data
            })

    def govno_chart(self, collection):
        cursor = self.db[collection].find()
        temp_data = []
        time_data = []
        for elem in cursor:
            temp_data.append(elem[collection])
            time_data.append(elem['Timestep'])
        return {'temp_data': temp_data, 'time_data': time_data}


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
