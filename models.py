from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    favorite_language: str
    years_experience: float