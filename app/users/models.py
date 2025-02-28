import enum

from pydantic import BaseModel


class EnumUserStatus(str, enum.Enum):
    activated = "activated"
    deactivated = "deactivated"

class User(BaseModel):
    id: int
    username: str
    role: str
    # TODO: make it hashed_password
    contact_number: str
    password: str
    barangay_at: str
    prompts: str
    status: EnumUserStatus

