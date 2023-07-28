import subprocess
from datetime import datetime
from typing import Optional

import jwt
from croniter import croniter
from crontab import CronTab
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

import config
import crud
import models
import schemas
from database import SessionLocal, engine
from security import verify_password, generate_token, validate_token, check_token_expired
from googletrans import *
import constant

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "https://reactjs-megasop.vercel.app",
    "https://react.thanhdev.info"
]

SECURITY_ALGORITHM = 'HS256'
SECRET_KEY = '123456'

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/search/{keyWord}")
async def search_taobao(keyWord: str):
    # translator = Translator()
    # # Chuyển tất cả về tiếng Anh để việc dịch gần đúng nhất
    # keyWordTranslateFirst = translator.translate(keyWord, dest=constant.ENGLISH).text
    # keyWordTranslateSecond = translator.translate(keyWordTranslateFirst, dest=constant.CHINESE).text
    # print(keyWordTranslateFirst)
    # print(keyWordTranslateSecond)
    return await crud.crawl_taobao(keyWord)


