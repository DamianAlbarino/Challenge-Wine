from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/dataframe/")
def dataframe():
    df = pd.read_csv('https://storage.googleapis.com/the_public_bucket/wine-clustering.csv')
    df = df.to_dict(orient='dict')
    return df