from typing import Optional

from fastapi_users import schemas

# Схема - абстракция, позволяющая структурировать объекты в бд

class UserRead(schemas.BaseUser[int]):
    """Класс-схема для считывания данных о пользователе"""
    id: int
    username: str
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    """Класс-схема для создания пользователя"""
    username: str
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
