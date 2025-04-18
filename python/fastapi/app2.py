import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import PlainTextResponse, JSONResponse # type: ignore # type: ignore
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, json_schema # type: ignore
from typing import Optional

app = FastAPI()

class RequestUserDto(BaseModel):
    nickname : str=Field(title='사용자 닉네임')
    email : EmailStr=Field(title='사용자 이메일 주소')                                          # email style인지 검사해줌.
    phone : str=Field(title='사용자 휴대폰  번호', pattern='^010-([0-9]{4})-([0-9]{4})$')       # 010 앞에 있는 ^ 의 의미 : 010으로 '시작하는'
    description : Optional[str]=Field(title='사용자 소개')                                      # 맨끝 $ : 0~9 숫자 4개로 '끝나는'

class ResponseUserDto(BaseModel):
    nickname : str=Field(title='사용자 닉네임')
    email : EmailStr=Field(title='사용자 이메일 주소')
    phone : str=Field(title='사용자 휴대폰  번호', pattern='^010-([0-9]{4})-([0-9]{4})$')
    description : Optional[str]=Field(title='사용자 소개')

    class Config:
        json_schema_extra = {
            'example': {
                'nickname': '왓슨',
                'email': 'watson@example.com',
                'phone': '010-1234-5678',
                'description': '버즈니 왓슨입니다.'
            }
        }

@app.get(
    path='/', description='HelthCheck용 포인트 입니다.',
    status_code=status.HTTP_200_OK,                           # status 상태를 보고 싶으면, 200, 201과 같이 특별한 숫자로 지정하는 것이 좋음.
    response_class=PlainTextResponse,
    responses={200: {"description": "Health check 응답"}}
)
async def HealthCheck():
    return "{status: 'ok'}"

@app.post(
    path='/registerReq', 
    description='회원가입 API입니다.',
    status_code=201,                                   # status 코드를 사용자가 지정해서 쓸 수 있음 
    response_class=JSONResponse,                       # [200: 성공, 300 : 리다이렉션(Redirection), 400: 실패 , 500: 서버 에러 (대부분 코드 문제)]
    responses={
        201: {
            "description":"가입 사용자 정보",
            "content": {
                "application/json": {
                    "example": {
                        "nickname": "왓슨",
                        "email": "watson@example.com",
                        "phone": "010-1234-5678",
                        "description": "버즈니 왓슨입니다."
                    }
                }
            }
        }
    }
)
async def register_req_user(req: RequestUserDto):
    return req.dict()

@app.post(
    path='/registerRes',
    description='회원가입 API입니다.',
    status_code=201,
    response_model = ResponseUserDto,
    responses={
        200: {
            "description": "가입 사용자 정보"
        }
    }
)
async def register_res_user(req: ResponseUserDto):
    return req.dict()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=3000)
