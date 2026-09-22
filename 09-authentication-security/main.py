from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from pwdlib import PasswordHash
import jwt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
security = HTTPBearer()
password_hash = PasswordHash.recommended()
users = {}

class User(BaseModel):
    username: str
    password: str 

@app.post("/register")
def register_user(user: User):
    hashed_password = password_hash.hash(user.password)
    users[user.username] = hashed_password
    return {
    "username": user.username
}

@app.post("/login")
def login_user(user: User):
    stored_hash = users.get(user.username)
    if stored_hash is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    password_matches = password_hash.verify(user.password, stored_hash)
    if not password_matches:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = jwt.encode(
    {"sub": user.username},
    "secret-key",
    algorithm="HS256"
)
    return {
    "access_token": token
}

@app.get("/protected")
def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, "secret-key", algorithms=["HS256"])
        username = payload["sub"]

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return {
        "message": f"Welcome {username}, you accessed protected data"
    }