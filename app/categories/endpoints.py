from fastapi import APIRouter, Depends

from app.categories import crud
from app.fake_db import FakeDB, get_fake_db

router = APIRouter()

@router.get("/")
def get_categories(fake_db: FakeDB = Depends(get_fake_db)):
    return crud.get_categories(fake_db)

@router.get("/{category_id}")
def get_category(category_id: int, fake_db: FakeDB = Depends(get_fake_db)):
    return crud.get_category(fake_db, category_id)
