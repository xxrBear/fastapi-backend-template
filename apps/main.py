"""统一注册路由"""

from fastapi import APIRouter

from apps import apis

api_router = APIRouter()
api_router.include_router(apis.user.router, prefix="/api/user", tags=["user"])
api_router.include_router(apis.login.router, tags=["login"])
