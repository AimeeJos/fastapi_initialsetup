from fastapi import FastAPI
from routers import hello, auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(hello.router)
