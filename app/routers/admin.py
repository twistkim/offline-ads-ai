from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def dashboard():
    return {"admin": "admin dashboard (stub)"}