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
    roles: str
    avatar: str

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


class ServiceCreate(ServiceBase):
    pass


class Service(ServiceBase):
    id: int

    class Config:
        orm_mode = True


# Schéma de la class chatbox (chatbox)

class ChatboxBase(_pydantic.BaseModel):
    user_id: int
    pseudo: str
    message: str


class ChatboxCreate(ChatboxBase):
    pass


class Chatbox(ChatboxBase):
    id: int

    class Config:
        orm_mode = True


# Schéma de la class facture (Facture)

class FactureBase(_pydantic.BaseModel):
    user_id: int
    description: str
    pdf: str


class FactureCreate(FactureBase):
    pass


class Facture(FactureBase):
    id: int

    class Config:
        orm_mode = True


# Schéma de la class devis (Devis)

class DevisBase(_pydantic.BaseModel):
    user_id: int
    description: str
    pdf: str


class DevisCreate(DevisBase):
    pass


class Devis(DevisBase):
    id: int

    class Config:
        orm_mode = True
