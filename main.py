#Fastapi

from fastapi import FastAPI

# Python

from dotenv import load_dotenv

# Locales

from routes.auth import auth_routes
from routes.users_github import users_github


app = FastAPI()

app.include_router(auth_routes, prefix = "/api")
app.include_router(users_github, prefix = "/api")

load_dotenv()
