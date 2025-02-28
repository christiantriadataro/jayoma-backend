from app.fake_db import FakeDB


def get_categories(fake_db: FakeDB):
    return fake_db.get_categories()

def get_category(fake_db: FakeDB, category_id: int):
    return fake_db.get_category(category_id)