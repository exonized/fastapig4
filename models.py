from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import passlib.hash as _hash
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    pseudo = Column(String, unique=True, index=True)
    roles = Column(String,  default=('Membre'))
    avatar = Column(String, default=('Avatar/base.png'))
    hashed_password = Column(String)

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.hashed_password)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, index=True)
    description = Column(String, index=True)
    prix = Column(Integer, index=True)
    image = Column(String, index=True)


class Contact(Base):
    __tablename__ = "contact"
    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, index=True)
    description = Column(String, index=True)
    user_id = Column(Integer, index=True)
    image = Column(String, index=True)


class Services(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, index=True)
    descripion = Column(String, index=True)
    image = Column(String, index=True)
    prix = Column(Integer, index=True)
