from fastapi import FastAPI, status
from sqlalchemy.orm import Session

from sqlalchemy import MetaData, Table
from sqlalchemy.orm import declarative_base

from numpy import average, record

from datetime import datetime
from dateutil.relativedelta import relativedelta

from pydantic import BaseModel
from odmantic import Model
from db_conn import engineconn
import json
from model import (
    ImgMetaData
)

from meta_scraper import MetaScraper

app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()


######## 시작 ########
@app.get("/")
async def first_get():

    hi = "하이하이!!"
    return hi


# img_meta_data
@app.post("/send_meta_data")
async def send_meta_data(path: str, latitude: str, longitude: str, manufacturer:  str, length: str, width: str):
    ms = MetaScraper()
    table = "img_meta_data"

    json_data = {
        "path": path,
        "latitude": latitude,
        "longitude": longitude,
        "manufacturer": manufacturer,
        "length": length,
        "width": width
    }

    try:
        json.dump(json_data)
        # meta_test = ms.search()
        # print(meta_test)

        # for h in haccp:
        #     print(h)
        #     session.bulk_insert_mappings(ImgMetaData, h)

        # session.commit()
        

    except Exception as e:
        print("img_meta_data", e)
    

    return json_data
