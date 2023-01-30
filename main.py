
from fastapi import FastAPI, status, Body, Depends, Header, Cookie
from typing import Optional
# from sqlalchemy.orm import Session
# from sqlalchemy import MetaData, Table
from sqlalchemy.orm import declarative_base

from fastapi import FastAPI, Body, Depends
from app.schema import UserSchema, MetaSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer

from db_conn import engineconn
from typing import List
from app.model import (
    ImgMetaData,
    BppleUser
)
from app.schema import *

app = FastAPI()
app.router.redirect_slashes = False

############################ DB ############################
engine = engineconn()
session = engine.sessionmaker()
############################################################

################ 데이터 append 되는 리스트 #################
users: List[UserSchema] = [
    {"id": "test",
    "pw": "1234",
    "farm_name": "펭귄농장"
    }
]
# metas: List[MetaSchema] = []
############################################################
access_token: bytes

# 시작
@app.get("/", tags=["start"], status_code=status.HTTP_201_CREATED)
async def root():
    hi = {"hello": "world!"}

    return {
            "code": "0000",
            "msg": "hello!"
        }

@app.get("/secretInfo/", tags=["start"])
async def secret_info(header: Optional[str] = Header(None)):
    print(access_token)
    
    return {
            "token": access_token,
        }

# 회원 아이디로 조회
# 디비에서 다시 조회해야 함 
@app.get("/posts/{id}/", tags=["search id"], status_code=status.HTTP_201_CREATED)
def get_one_post(id: str): # 여기에 아이디 값을 입력
    # 아이디가 post에 있다면
    for user in users:
        user_dict = user.dict() # 객체가 들어갔기 때문에 dic형식으로 변환
        if user_dict["id"] == id:
            return {
                "data": user
            }
        else:
            return {"result": "회원 아이디가 존재하지 않습니다."}


# 유저 회원가입
@app.post("/signup/", tags=["user"])
def user_signup(user: UserSchema=Body(default=None), status_code=status.HTTP_201_CREATED):
    users.append(user)

    return signJWT(user.id) # 회원가입 후 토큰 생성


# 회원가입 후 유저정보 DB넣기
@app.get("/insert_user/", tags=["Insert User"])
async def insert_user():
    for user in users:
        session.bulk_insert_mappings(BppleUser, [user.dict()])
        session.commit()

    session.add
    print(users)

    return users


# 유저 로그인 유효성 검사
def check_user(data: UserLoginSchema):
    print(data)
    for user in users:
        print(user)
        if user['id'] == data.id and user['pw'] == data.pw:
            return True

        return False


@app.post("/login/", tags=["user"], status_code=status.HTTP_201_CREATED)
def user_login(user: UserLoginSchema=Body(default=None)): # 바디에 담아서 보낸다
    print("유저 타입:", type(user))

    if check_user(user):
        token = signJWT(user.id) # 로그인 후 토큰 생성
        
        print(type(token["access token"]))
        global access_token
        access_token = token["access token"]
        
        return {
            "code": "0001",
            "msg": "로그인 성공!",
            "token": access_token
        }
    else: 
        return {
            "code": "0000",
            "msg": "유효하지 않은 로그인",
            "token": None
        }
    

# 이미지 메타데이터 보내기 > 토큰 있어야 가능
# @app.post("/send_meta_data/", dependencies=[Depends(jwtBearer())], tags=["send metadata"])
@app.post("/send_meta_data/", tags=["send metadata"])
async def send_meta_data(meta: MetaSchema=Body(default=None)):
    print("원본", meta)
    dic = meta.dict()
    meta = dic["meta"]
    
    session.bulk_insert_mappings(ImgMetaData, meta)
    session.commit()

    # session.add
    # print(item.dict())
        
    return {
        "token": "www"
    }