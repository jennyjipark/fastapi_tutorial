from pydantic import BaseModel, Field
from typing import List
from datetime import datetime, timezone

# 메타정보 스키마
class MetaItemSchema(BaseModel):
    file_path: str = Field(default=None) 
    upload_time: datetime = Field(default=None) 
    capture_time: datetime = Field(default=None) 
    file_path: str = Field(default=None) 
    latitude: str = Field(default=None)
    longitude: str = Field(default=None)
    manufacturer: str = Field(default=None)
    length: str = Field(default=None)
    width: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "file_path": "img/img/img...",
                "upload_time": "2022-12-01",
                "capture_time": "2022-12-01",
                "latitude": "37.1010100",
                "longitude": "10.0000000",
                "manufacturer": "samsung",
                "length": "1000",
                "width": "2000",
            }
        }

class MetaSchema(BaseModel):
    meta: List[MetaItemSchema] = Field(default=None)


# 유저정보 스키마
class UserSchema(BaseModel):
    id: str = Field(default=None)
    pw: str = Field(default=None)
    farm_name: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "id": "test",
                "pw": "1234",
                "farm_name": "비굿농원"
            }
        }

# 유저 로그인 스키마
class UserLoginSchema(BaseModel):
    id: str = Field(default=None)
    pw: str = Field(default=None)
    
    class Config:
        the_schema = {
            "user_demo": {
                "id": "test_id",
                "pw": "123"
            }
        }

