from fastapi import FastAPI
from app.categories import endpoints as category_endpoints

CATEGORIES_ENDPOINT = "/categories"
USERS_ENDPOINT = "/users"
ORDINANCES_ENDPOINT = "/ordinances"

app = FastAPI()
app.include_router(category_endpoints.router, prefix=CATEGORIES_ENDPOINT, tags=["categories"])
@app.get("/")
def read_root():
    return {"message": "Welcome to Jayoma Bot"}