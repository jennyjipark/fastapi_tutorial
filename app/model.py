from curses import meta
from importlib.metadata import MetadataPathFinder, metadata
from unicodedata import category
from pydantic import BaseModel
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    null,
    Sequence,
    Table,
    MetaData,
    Identity,
    Numeric,
    CHAR
)

# from pydantic import BaseModel
from sqlalchemy.orm import declarative_base

Base = declarative_base()
meta = MetaData()


class ImgMetaData(Base):
    __tablename__ = "test_bpple_meta" # 여기서 테이블명은 소문자로 만들어야 한다.

    seq = Column(Integer, primary_key=True, autoincrement=True)
    uplode_time = Column(DateTime, nullable=False) # 업로드 시각
    capture_time = Column(DateTime, nullable=False) # 사진찍은 시각
    file = Column(String(200), nullable=True)  # 파일경로
    latitude = Column(String(50), nullable=True)  # 위도
    longitude = Column(String(50), nullable=True)  # 경도        
    manufacturer = Column(String(50), nullable=True)  # 제조사
    length = Column(String(50), nullable=True)  # 길이
    width = Column(String(50), nullable=True)  # 높이

class BppleUser(Base):
    __tablename__ = "test_bpple_user"

    seq = Column(Integer, primary_key=True, autoincrement=True)
    register_time = Column(DateTime, nullable=False) # 회원가입 시각
    id = Column(String(50), nullable=True)  # 아이디
    pw = Column(String(50), nullable=True)  # 패스워드
    farm_name = Column(String(50), nullable=True)  # 농장명
    

    
