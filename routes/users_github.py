# Fastapi

from fastapi import APIRouter

# Pydantic

from pydantic import BaseModel

# Python

from requests import get

# Internal Functions

from middleware.verify_token_route import VerifyTokenRoute


users_github = APIRouter(route_class = VerifyTokenRoute)

# Model

class UserGithub(BaseModel):
    country: str
    page: str
    

# Route conection Api github

@users_github.post("/users/github")
def github_users(github: UserGithub):
    return get(f'https://api.github.com/search/users?q=location:"{github.country}"&page={github.page}').json()
    
