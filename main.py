from fastapi import FastAPI
from routers import hello, auth, users, medicines

app = FastAPI()

app.include_router(auth.router)
app.include_router(hello.router)
app.include_router(users.router)
app.include_router(medicines.router)
