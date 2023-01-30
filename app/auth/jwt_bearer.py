# 요청이 승인되었는지 여부를 확인

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .jwt_handler import decodeJWT


# 인증을 유지하는데 사용
class jwtBearer(HTTPBearer):
    def __init__(self, auto_Error: bool = True):
        super(jwtBearer, self).__init__(auto_error=auto_Error) #HTTPBearer의 모든 것을 상속

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(jwtBearer, self).__call__(request)
        print("scheme 모야!! ", credentials)
        if credentials:
            if not credentials.scheme == "Bearer":
                print("여기서 걸리네")
                raise HTTPException(status_code=403, detail="Invalid or Expired Token!")
                
            return credentials.credentials
        else:
            print("여기인가?")
            raise HTTPException(status_code=403, details="Invalid or Expired Token!")

    def verify_jwt(self, jwtoken: str):
        isTokenValid: bool = False # A false flag
        # isToken이 유효한지 확인

        payload = decodeJWT(jwtoken)

        if payload: # 트루라면
            isTokenValid = True
        return isTokenValid