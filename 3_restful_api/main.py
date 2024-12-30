import uvicorn
from fastapi import FastAPI
from results import router_results
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_results, prefix="/api", tags=["Results"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)