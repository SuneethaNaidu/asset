from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AssetFlow AI",
    description="Enterprise Asset & Resource Management System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "success": True,
        "application": "AssetFlow AI",
        "version": "1.0.0",
        "message": "Backend Running Successfully"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }
