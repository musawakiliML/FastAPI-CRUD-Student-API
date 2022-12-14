from fastapi import FastAPI

from server.routes.student import router as StudentRouter

# Creating base instance
app = FastAPI()

app.include_router(StudentRouter, tags=["Student"], prefix="/student")

@app.get('/', tags=["Root"])
async def read_root():
    return {"Message": "Welcome to My Student CRUD APP"}