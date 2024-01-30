from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/getDataFrame/{url}")
def dataframe(url:str):
    df = pd.read_csv(url)          # Leo el url
    df = df.to_dict(orient='dict') # Lo pasa a formato diccionario, que es identico al formato de un json.
    return df