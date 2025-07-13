from pydantic import BaseModel

class UserSignupRequest(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str
    gender: str

class UsersSingupResponse(BaseModel):
    message: str 
