from crud.user import user_signup
from schemas.user import UserSignupRequest

def user_signup_request(user_details: UserSignupRequest):
    return user_signup(
        user_details.firstName,
        user_details.lastName,
        user_details.email,
        user_details.password,
        user_details.gender
    )
