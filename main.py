
from fastapi import FastAPI, status, Body, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import declarative_base
from numpy import average, record

from datetime import datetime
from dateutil.relativedelta import relativedelta

from pydantic import BaseModel
from odmantic import Model
from db_conn import engineconn
import json
from typing import List
from starlette.responses import JSONResponse
from model import (
    ImgMetaData,
    BppleUser
)

from meta_scraper import MetaScraper

app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()




class Item(BaseModel):
    path: str
    latitude: str
    longitude: str
    manufacturer: str
    length: str
    width: str

class User(BaseModel):
    id: str
    pw: str
    farm_name: str

user_info: List[User] = []

# user_info: List[User] = [
    # User(
    #     id = "test01", 
    #     pw = "0000",
    #     farm_name = "테스트",
    #  ),

    #  User(
    #     id = "test02", 
    #     pw = "0000",
    #     farm_name = "테스트",
    #  )
# ]


######## 시작 ########
@app.get("/")
async def first_get():

    hi = "하이하이!!"
    return hi


# 이미지 메타데이터 보내기
@app.post("/send_meta_data")
async def send_meta_data(item: Item):
    item_dict = item.dict()
    return item_dict


# 유저 정보 보내기
@app.post("/send_user")
async def send_meta_data(user: User):
    user_info.append(user)

    return user

# 유저정보 DB넣기
@app.get("/get_user")
async def get_user():
    for u in user_info:
        session.bulk_insert_mappings(BppleUser, [u.dict()])
        session.commit()

    return user_info


# @app.put("/get_meta_data/{item_id}")
# async def get_meta_data(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}
