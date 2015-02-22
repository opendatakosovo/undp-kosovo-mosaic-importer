# -*- coding: utf-8 -*-

import csv
import os
from datetime import datetime, date
from slugify import slugify
from pymongo import MongoClient
from utils import Utils

# Connect to default local instance of mongo
client = MongoClient()

# Get database and collection
db = client.undpkosovomosaic
collection = db.mosaic
utils = Utils()
collection.remove({})

def parse():

    print "Importing UNDP KOSOVO MOSAIC DATA."

        with open('data/'+ filename, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            line_number = 0
            for row in reader:
                year = int(filename.replace('.csv', ''))
                budget_type = convert_buget_type(row[0])
      
                report = {
                    "komuna": {
                  
                }

                collection.insert(report)


parse()
