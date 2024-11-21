import os

AWS_S3_BUCKET_NAME = 'SENSOR FAULT DETECTION'
MONGO_DATABASE_NAME= "fault"
MONGO_COLLECTION_NAME = "sensordata"

TARGET_COLUMN = 'quality'
MONGO_DB_URL = 'mongodb+srv://Nitish:YGDJZkAsIay2oDr6@faultdetect.kadz1.mongodb.net/?retryWrites=true&w=majority&appName=faultdetect'

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION =".pkl"

artfacts_folder ='Artifacts'