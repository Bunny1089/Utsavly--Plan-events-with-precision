from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import settings, APP_NAME
from backend.database import Base, engine
from backend.routers import events, budget, timeline, vendors, ideas, health, copilot

# Initialize SQLite database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=f"{APP_NAME} API",
    description="GenAI-powered Indian Event Planning Assistant Backend",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routers under /api
app.include_router(events.router, prefix="/api")
app.include_router(budget.router, prefix="/api")
app.include_router(timeline.router, prefix="/api")
app.include_router(vendors.router, prefix="/api")
app.include_router(ideas.router, prefix="/api")
app.include_router(health.router, prefix="/api")
app.include_router(copilot.router, prefix="/api")

@app.get("/")
def root():
    return {
        "app": APP_NAME,
        "status": "online",
        "mock_mode": settings.ai_mock,
        "docs_url": "/docs"
    }

@app.get("/api/health")
def api_health():
    return {
        "status": "healthy",
        "app": APP_NAME,
        "mock_mode": settings.ai_mock
    }
