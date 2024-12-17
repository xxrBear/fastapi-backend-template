"""统一注册路由"""
from fastapi import APIRouter

from app import user

api_router = APIRouter()
api_router.include_router(user.api.router, prefix="/api/user", tags=["user"])
