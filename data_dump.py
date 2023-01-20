import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.a1alg.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = '/Users/dipanwitabiswas/Desktop/ML_Projects/ML_Project_Insurance/insurance.csv'
DATABASE_NAME='insurance'
COLLECTION_NAME='tbl_insurance'


if __name__=='__main__' :
    df = pd.read_csv(DATA_FILE_PATH)
    #remove the index
    df.reset_index(drop=True, inplace=True)
    json_data=df.to_dict(orient='records')

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_data)
