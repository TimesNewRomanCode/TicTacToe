from fastapi import FastAPI
from app.routers import router

app = FastAPI(title="TicTacToe")
app.include_router(router)