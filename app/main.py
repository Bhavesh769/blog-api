from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.routers import users
from app.routers import posts
from app.routers import comments


Base.metadata.create_all(bind=engine)


app = FastAPI(title="Blog API")

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comments.router)
