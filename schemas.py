from typing import Union
import pydantic as _pydantic

# Schéma de la class Item (Articles)


class ItemBase(_pydantic.BaseModel):
    titre: str
    description: Union[str, None] = None
    prix: int
    image: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


# Schéma de la class Utilisateur (Users)


class _UserBase(_pydantic.BaseModel):
    email: str
    pseudo: str
    avatar: str
    roles: str
    adresse: str
    complement: str
    codepostal: int
    region: str
    numerorue: int


class UserCreate(_UserBase):
    hashed_password: str

    class Config:
        orm_mode = True


class User(_UserBase):
    id: int

    class Config:
        orm_mode = True


# Schéma de la class Contact (Contact)


class ContactBase(_pydantic.BaseModel):
    titre: str
    description: Union[str, None] = None
    user_id: int
    image: str


class ContactCreate(ContactBase):
    pass


class Contact(ContactBase):
    id: int

    class Config:
        orm_mode = True


# Schéma de la class services (Services)

class ServiceBase(_pydantic.BaseModel):
    titre: str
    description: Union[str, None] = None
    image: str


class ServiceCreate(ItemBase):
    pass


class Service(ItemBase):
    id: int

    class Config:
        orm_mode = True


# Schéma de la class email (email)
