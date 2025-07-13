from fastapi import APIRouter
from schemas.chat import ChatRequest, ChatResponse
from services.chat_service import get_ai_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(chat_request: ChatRequest):
    ai_reply = get_ai_response(chat_request.user_message)
    return ChatResponse(ai_response=ai_reply)
