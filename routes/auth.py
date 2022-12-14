# Fastapi

from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from fastapi import status


# Pydantic

from pydantic import BaseModel, EmailStr


# Internal Functions

from functions_jwt import write_token, validate_token


auth_routes = APIRouter()


#Models

class User(BaseModel):
    username: str
    email: EmailStr
    
## Example
   
    class Config:
        schema_extra = {
            'example': {      
                'username': 'Erika Alvarez',
                'email': 'erika@gmail.com'
                }
        }
            
            
#Routes

## Login

@auth_routes.post("/login")
def login(user: User):
    print(user.dict())
    if user.username == "Erika Alvarez":
        return write_token(user.dict())
    else:
        return JSONResponse(content = {"message": "User not found"}, status_code = status.HTTP_404_NOT_FOUND)
    
    
## Verification Token        
    
@auth_routes.post("/verify/token")
def verify_token(Authorization: str = Header(None)): 
    token = Authorization.split(" ")[1]       
    return validate_token(token, output=True)
    
     