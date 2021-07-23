from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api.v1.api import api_router
import uvicorn
# from app.util.config_util import config

app = FastAPI(
    title="Fast APi template"
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

#to run project go to app folder and
#to run project in windows: python -m main
#to run project in linux: python3 main.py
if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)