from typing import Union

from fastapi import FastAPI

from dotenv import load_dotenv
import os
load_dotenv()

app = FastAPI()

DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_SCHEMA = os.environ.get('DB_SCHEMA')
DB_PORT = os.environ.get('DB_PORT')

DB_URL = 'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_SCHEMA}'
@app.get("/")
def read_root():
    mySecret = os.environ.get('MySecret')
    return {"Hello": "123"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
