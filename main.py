import os
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.config import Config
from authlib.integrations.starlette_client import OAuth
from dotenv import load_dotenv
from api.v1.endpoints import chat, user
from db.connection import get_connection 

# Load env vars
load_dotenv()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
SESSION_SECRET = os.getenv("SESSION_SECRET", "74RKcRlqyOeXjDQV6rGAdCt6tOJgIfZMzl1qO0M4kr3Zp0vjEPvxiSYCj0zJZDXm")

print('google client id:', os.environ.get('GOOGLE_CLIENT_ID'))  # Must not be None

oauth = OAuth()


oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'},
)

# FastAPI App
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=SESSION_SECRET)

get_connection()

# Routers
prefix = "/api/v1"
app.include_router(chat.router, prefix=prefix)
app.include_router(user.router, prefix=prefix)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Therapist Assistant"}

# Google Login Route
@app.get("/login/google")
async def login_via_google(request: Request):
    google = oauth.create_client('google')
    redirect_uri = request.url_for('auth_via_google')
    return await google.authorize_redirect(request, redirect_uri)

# Google OAuth Callback
@app.get("/auth/google/callback")
async def auth_via_google(request: Request):
    google = oauth.create_client('google')
    token = await google.authorize_access_token(request)
    user = token['userinfo']

    # Redirect user to frontend with info
    return RedirectResponse(f"http://localhost:5500/home.html?name={user['name']}&email={user['email']}")

