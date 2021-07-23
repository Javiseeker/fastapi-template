from fastapi import APIRouter

from endpoints import example, ping

api_router = APIRouter()
api_router.include_router(example.router, prefix="/example", tags=["example"])
api_router.include_router(ping.router, prefix="/ping", tags=["ping"])