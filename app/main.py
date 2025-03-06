"""统一注册路由"""

from fastapi import APIRouter

from app import apis

api_router = APIRouter()
api_router.include_router(apis.user.router, prefix="/api/user", tags=["user"])
