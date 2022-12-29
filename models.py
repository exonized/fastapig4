from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import passlib.hash as _hash
from database import Base


class User(Base):
    __tablename__ = "Utilisateurs"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    pseudo = Column(String, unique=True, index=True)
    roles = Column(String,  default=('Membre'))
    avatar = Column(String, default=('Avatar/base.png'))
    hashed_password = Column(String)
    adresse = Column(String)
    completement = Column(String)
    codepostal = Column(Integer)
    region = Column(String)
    numerorue = Column(Integer)

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.hashed_password)


class Item(Base):
    __tablename__ = "Produits"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, index=True)
    description = Column(String, index=True)
    prix = Column(Integer, index=True)
    image = Column(String, index=True)


class Devis(Base):
    __tablename__ = "Devis"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    description = Column(String)
    pdf = Column(String)


class Facture(Base):
    __tablename__ = "Facture"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    description = Column(String)
    pdf = Column(String)


class Feedback(Base):
    __tablename__ = "Feedback"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    ratting_feedback = Column(Integer)
    titre_feedback = Column(String)
    contenu_feedback = Column(String)


class Contact(Base):
    __tablename__ = "Contact"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    objet = Column(String, index=True)
    message = Column(String, index=True)


class Services(Base):
    __tablename__ = "Services"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, index=True)
    descripion = Column(String, index=True)
    image = Column(String, index=True)
    prix = Column(Integer, index=True)


class Chatbox(Base):
    __tablename__ = "Chatbox"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    pseudo = Column(String)
    message = Column(String)


class Commandes(Base):
    __tablename__ = "Commandes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    articles_id = Column(Integer)


class Articles(Base):
    __tablename__ = "Articles"
    id = Column(Integer, primary_key=True, index=True)
    types = Column(String)
    titre = Column(String)
    description = Column(String)
    contenu = Column(String)
    images = Column(String)
