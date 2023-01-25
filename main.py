from fastapi import FastAPI, status, Body
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
from starlette.responses import JSONResponse
from model import (
    ImgMetaData
)

from meta_scraper import MetaScraper

app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()


######## 시작 ########
# @app.post("/")
# async def first_get():

#     hi = "하이하이!!"
#     return hi


# img_meta_data
@app.get("/send_meta_data")
# 매개변수를 객체 하나로 만드는게 좋을듯
async def send_meta_data( path: str = Body(), latitude: str = Body(), longitude: str = Body(), manufacturer:  str = Body(), length: str = Body(), width: str = Body()):
    ms = MetaScraper()
    table = "img_meta_data"
# path: str, latitude: str, longitude: str, manufacturer:  str, length: str, width: str
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
    

    return JSONResponse(json_data)
