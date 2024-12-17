from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request

from app.main import api_router
from common import state
from common.execptions import ValidateError, validate_exception_handler
from common.resp import json_data

app = FastAPI()
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # 允许的来源
    allow_credentials=True,  # 是否允许发送 Cookie
    allow_methods=["*"],  # 允许所有 HTTP 方法 (GET, POST, DELETE 等)
    allow_headers=["*"],  # 允许所有请求头
)
app.add_middleware(SessionMiddleware, secret_key='secret')

app.add_exception_handler(ValidateError, validate_exception_handler)


@app.exception_handler(ValidateError)
async def unicorn_exception_handler(request: Request, exc: ValidateError):
    return json_data(code=state.REQUEST_PARAMS_ERROR, message=exc.name)