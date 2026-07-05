from fastapi import FastAPI

from api.webhook import router

server = FastAPI()

server.include_router(router)