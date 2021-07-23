from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def ping() -> Any:
    return "pong"

@router.get("/2")
async def ping() -> Any:
    return "pong2"