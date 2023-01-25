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

    hi = "hello"
    return hi


# img_meta_data
@app.get("/img_meta_data")
def get_img_meta_data():

    meta_scraper = MetaScraper()
    table = "img_meta_data"

    # try:
    #     img = meta_scraper.search()
        # print(haccp)
        # for h in haccp:
            # print(h)
            # session.bulk_insert_mappings(ConsumerHaccp, h)

        # session.commit()
        # fvc(f"테이블명: {table}", f"{time} 데이터 insert 완료")

    # except Exception as e:
    #     print("img_meta_data", e)
    #     fvc(f"테이블명: {table}", f"{time} 데이터 insert를 완료하지 못했습니다.")
    # log_txt(table)

    return "뭔 개소리야"
