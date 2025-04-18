from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def HealthCheck():
    return {"status":"ok"}

@app.get('/hello')
async def Hello():
    return {"message": "Hello World~!!"}

@app.post('/random')                           # decoration이라고 칭함. ,, 이 함수를 만들고 get, post를 만들 필요가 없음.          
@app.get('/random')                            # decoration이 함수 내부로 접근함.
async def Random(max=None):
    import random

    if max in None:
        max = 10
    else:
        max = int(max)
    return {"random number": random. randint(1, max)}