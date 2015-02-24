import csv
from pymongo import MongoClient

# Connect to default local instance of mongo
client = MongoClient()

# Get database and collection
db = client.undpkosovomosaic
collection = db.mosaic
collection.remove({})

DATAFILE = "data/Mosaic-2012.csv"


def parse_file(datafile):

    with open(datafile, "r") as f:
        reader = csv.reader(f, delimiter=',')
        # Save the header of the CSV file which usually
        # contains the keys(descriptions or columns)
        header = reader.next()
        print('Importing data.')
        # Iterate the file line by line, not including first line
        # because we called .next() on the header and it skiped 1'st line
        for row in reader:

            # Create a dictionary to build the document
            dictionary = {}

            # Attach each element of the header list with the
            # elements of the row list
            for h, v in zip(header, row):
                #print h + " : " + v
                dictionary[h] = v

            # Add document to MongoDB
            collection.insert(dictionary)
        print('.')


parse_file(DATAFILE)
