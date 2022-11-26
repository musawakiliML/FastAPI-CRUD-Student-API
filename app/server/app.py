from fastapi import FastAPI


# Creating base instance
app = FastAPI()

@app.get('/', tags=["Root"])
async def read_root():
    return {"Message": "Welcome to My Student CRUD APP"}