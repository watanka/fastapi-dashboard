from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.question import question_router

app = FastAPI()

origins = [
    'http://localhost:5173' # frontend에서 fastapi 서버가 제공한 정보를 사용할 수 있도록
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
    )

app.include_router(question_router.router)