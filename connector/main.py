

import pymongo
import pandas as pd


MONGO_DB_URL = "mongodb+srv://cloud-gaurav:Kabali1234@cluster0.5scda40.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(MONGO_DB_URL)

# database connection

db = client["self-projects"]
collection = db["sensor_data"]

all_records = collection.find()

## iterate over all records

for row in all_records:
    print(row)
    
all_records = collection.find()

list_cursor = list(all_records)

# Read as dataframe

df = pd.DataFrame(list_cursor)

df.drop(columns="_id", axis=1)

print(df)

# Exporting as csv file

df.to_csv("dataset.csv")

print("Data exported successfully")