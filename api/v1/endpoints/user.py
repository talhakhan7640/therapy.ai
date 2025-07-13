from fastapi import APIRouter 
from schemas.user import UserSignupRequest, UsersSingupResponse
from services.user_service import user_signup_request

router = APIRouter()

@router.post("/signup", response_model= UsersSingupResponse)
def signup_endpoint(user_details: UserSignupRequest):
    return user_signup_request(user_details)
