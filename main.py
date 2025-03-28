from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from apps.main import api_router

app = FastAPI()
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许的来源
    allow_credentials=True,  # 是否允许发送 Cookie
    allow_methods=["*"],  # 允许所有 HTTP 方法 (GET, POST, DELETE 等)
    allow_headers=["*"],  # 允许所有请求头
)
app.add_middleware(SessionMiddleware, secret_key="secret")
