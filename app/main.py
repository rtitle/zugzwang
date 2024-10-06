from fastapi import FastAPI

from app.api.main import api_router

app = FastAPI(title="Project Zugzwang")
app.include_router(api_router)
