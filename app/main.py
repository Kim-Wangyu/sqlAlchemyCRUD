# from msilib.schema import Directory
# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from pathlib import Path
# from app.routers import crud


# BASE_DIR = Path(__file__).resolve().parent


# app = FastAPI()
# app.include_router(crud.user)



# @app.get("/", response_class=HTMLResponse)
# async def root(request: Request):
#     return "hello"

from fastapi import FastAPI,Request, APIRouter
from app.routers import crud
from app.routers.crud import create_user
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import sessionmaker
from fastapi.responses import HTMLResponse, JSONResponse
from app.routers.crud import user_router

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)

# app.add_api_route(path="/users", methods=["GET", "POST", "PUT", "DELETE"], endpoint=create_user)
# app.add_api_route(path="/users", methods=["POST"], endpoint=create_user)


# Session= sessionmaker()
# Session.configure(bind=DATABASES)
# session=Session()

# test = users(1,"we","ew","we")

# session.add(test)
# session.commit()


@app.get("/", response_class=JSONResponse)
async def root(request: Request):
    return "hello"