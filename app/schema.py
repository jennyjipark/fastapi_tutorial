from pydantic import BaseModel, Field
from typing import List

# 메타정보 스키마
class MetaItemSchema(BaseModel):
    file: str = Field(default=None) 
    latitude: str = Field(default=None)
    longitude: str = Field(default=None)
    manufacturer: str = Field(default=None)
    length: str = Field(default=None)
    width: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "file": "img/img/img...",
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

