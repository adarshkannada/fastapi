from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "naav bando, naav bando"}

@app.get("/posts")
def get_posts():
    return {"data": "idu nanna postu"}

@app.post("/createpost")
def create_posts():
    return {"message": "hosa post haakiddivi"}