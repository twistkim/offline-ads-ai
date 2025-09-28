from fastapi import FastAPI
from app.routers import user, admin

# 앱 생성
app = FastAPI(
    title="Offline Ads AI",
    description="매체 소개서 등록 + 블로그 자동 글쓰기 서비스",
    version="0.1.0"
)

# 라우터 등록
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])


@app.get("/")
def root():
    return {"message": "Offline Ads AI API is running!"}