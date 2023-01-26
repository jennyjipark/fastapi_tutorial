
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from config import get_secret

class engineconn:

    app = {
    "name": "postgresql",
    "user": get_secret("POSTGRES_ID"),
    "password": get_secret("POSTGRES_PW"),
    "host": "bgood.c25k4phikwpu.ap-northeast-2.rds.amazonaws.com",
    "dbconn": "postgres",
    "port": "5432"
}
    conn_string = f'{app["name"]}://{app["user"]}:{app["password"]}@{app["host"]}:{app["port"]}/{app["dbconn"]}'

    def __init__(self):
        self.engine = create_engine(self.conn_string, pool_pre_ping=True)
        print("엔진", self.engine)
        
    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
        

    def connection(self):
        conn = self.engine.connect()
        return conn
