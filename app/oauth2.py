from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

#SECRET KEY
#algo
#expiration time


SECRET_KEY = "HELLO"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire =  datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt



def verify_acess_token(token:str, credentials_acception):
    
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        
        id: str = payload.get("user_id")
    
        if id is None:
            raise credentials_acception
        
        id = str(id)
        token_data =  schemas.TokenData(id=id)
    
    except JWTError:
        raise credentials_acception
    
    return token_data
    

def get_current_user(token:str= Depends(oauth2_scheme)):
    
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"could not validate credentials", headers={"WWW-Authentication" : "Bearer"})
     
    
    return verify_acess_token(token, credentials_exception)

    