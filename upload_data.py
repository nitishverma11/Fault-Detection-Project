from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri="mongodb+srv://Nitish:YGDJZkAsIay2oDr6@faultdetect.kadz1.mongodb.net/?retryWrites=true&w=majority&appName=faultdetect"

client = MongoClient(uri)

DATABASE_NAME="fault"
COLLECTION_NAME='sensordata'
df=pd.read_csv("C:\Users\abcd\Desktop\Fault Detection ML project\Notebook\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)
json_record=list(json.loads(df.T.to_json()).values())
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)