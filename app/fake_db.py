from typing import Dict, List

from app.categories.models import Category
# Public Safety and Order
# Business and Commerce
# Health and Sanitation
# Environmental Protection
# Public Welfare and Social Services
# Zoning and Land Use
# Education and Libraries
# Transportation and Infrastructure
# Tourism and Recreation
# Housing and Urban Development
from app.users.models import User

categories = [
    {
        "id": 1,
        "name": "Public Safety and Order",
    },
    {
        "id": 2,
        "name": "Business and Commerce",
    },
    {
        "id": 3,
        "name": "Health and Sanitation"
    },
    {
        "id": 4,
        "name": "Environmental Protection"
    },
    {
        "id": 5,
        "name": "Public Welfare and Social Services"
    },
    {
        "id": 6,
        "name": "Zoning and Land Use"
    },
    {
        "id": 7,
        "name": "Education and Libraries"
    },
    {
        "id": 8,
        "name": "Transportation and Infrastructure"
    },
    {
        "id": 9,
        "name": "Tourism and Recreation",
    },
    {
        "id": 10,
        "name": "Housing and Urban Development"
    }

]


class FakeDB:
    def __init__(self):
        self.categories_data = {
            "data": categories
        }
        # self.ordinances_data: Dict[str: List[Ordinance]] = {
        #     "data": []
        # }
        self.users_data: Dict[str, List[User]] = {
            "data": []
        }


    def get_categories(self):
            return self.categories_data

    def get_category(self, id: int) -> Category | Dict:
            response = [obj for obj in self.categories_data["data"] if obj.id == id]
            return response[0] if response else {}


def get_fake_db():
    db = FakeDB()
    # db.categories_data["data"] = categories
    return db