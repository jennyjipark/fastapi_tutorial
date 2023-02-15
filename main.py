
from fastapi import FastAPI, status, Body, Depends, Header, Cookie, UploadFile, File
from typing import Optional
# from sqlalchemy.orm import Session
# from sqlalchemy import MetaData, Table
from sqlalchemy.orm import declarative_base
from fastapi.responses import FileResponse
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
import os
from datetime import *

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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'static/')
IMG_DIR = os.path.join(STATIC_DIR, 'images/')
SERVER_IMG_DIR = os.path.join('http://localhost:8000/','static/','images/')

# 해당 폴더가 없을 경우 생성한다.
if not os.path.exists(STATIC_DIR):
    os.mkdir(STATIC_DIR)
if not os.path.exists(IMG_DIR):
    os.mkdir(IMG_DIR)

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
    print("원본", meta) # 리스트[객체]로 들어온다.
    dic = meta.dict() 
    meta = dic["meta"]
    
    try:
        session.bulk_insert_mappings(ImgMetaData, meta)
        session.commit()
    except Exception as e:
        print("send_meta_data error ", e)
        session.rollback()
    finally:
        session.close()

    # session.add
    # print(item.dict())
        
    return {
        "token": "www"
    }

# 이미지 서버로 보내기 > 토큰 있어야 가능
@app.post("/send_images/", tags=["send image"])
async def send_images(files: List[UploadFile] = File(...)):
# async def send_image(file: UploadFile = File(...)):
    print("파일들", files) 
    
    # file_urls = []

    # # 파일을 푼다.
    # for file in files:
    #     current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    #     saved_file_name = f"image_{current_time}"
    #     print(saved_file_name)

    #     file_location = os.path.join(IMG_DIR, saved_file_name)

    #     # 보낸 파일을 쓴다.
    #     with open(file_location, "wb+") as file_object:
    #         file_object.write(file.file.read())
    #     file_urls.append(SERVER_IMG_DIR + saved_file_name)

    # result = {"file_urls" : file_urls}
    
    return "file"

# 파일 저장
@app.get("/images/{file_name}", tags=["get images"])
def get_image(file_name:str):
    return FileResponse(''.join([IMG_DIR, file_name]))