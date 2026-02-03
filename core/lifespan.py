from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting application")
    app.state.db = "db-connection-placeholder"
    yield
    # Shutdown
    print("Shutting down application")
