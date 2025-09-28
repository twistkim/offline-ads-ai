from fastapi import APIRouter

router = APIRouter()

@router.get("/me")
def get_profile():
    return {"user": "current user profile (stub)"}