# this file is responsible for singing, endcoding, decoding and returning JWTs.
import time
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

# 생선된 토큰을 반환한다.
def token_response(token: str):
    return {
        "access token": token
    }

# 로그아웃 > 
# 토큰 생성
def signJWT(userID: str):
    payload = {
        "userID": userID,
        "expiry": time.time() + 20000 # 만료시간
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decode_token if decode_token["expires"] >= time.time() else None
    except Exception as e:
        print("decodeJWT 에러", e)
        return {}