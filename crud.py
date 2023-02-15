import sqlalchemy.orm as _orm

import passlib.hash as _hash
import jwt as jwtt
import fastapi
import fastapi.security as _security

import models
import schemas
import database


oauth2schema = _security.OAuth2PasswordBearer(tokenUrl="/api/token")
JWT_SECRET = "myjwtsecret"


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_user_by_email(email: str, db: _orm.Session):
    return db.query(models.User).filter(models.User.email == email).first()


async def create_token(user: models.User):
    user_obj = schemas.User.from_orm(user)

    token = jwtt.encode(user_obj.dict(), JWT_SECRET)

    return dict(access_token=token, token_type="bearer", roles=user.roles, email=user.email)


async def create_user(user: schemas.UserCreate, db: _orm.Session):
    user_obj = models.User(
        email=user.email, hashed_password=_hash.bcrypt.hash(user.hashed_password), pseudo=user.pseudo, adresse=user.adresse, complement=user.complement, codepostal=user.codepostal, region=user.region, numerorue=user.numerorue
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj


async def authenticate_user(email: str, password: str, db: _orm.Session):
    user = await get_user_by_email(db=db, email=email)

    if not user:
        return False

    if not user.verify_password(password):
        return False

    return user


async def get_current_user(
    db: _orm.Session = fastapi.Depends(get_db),
    token: str = fastapi.Depends(oauth2schema),
):
    try:
        payload = jwtt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = db.query(models.User).get(payload["id"])
    except:
        raise fastapi.HTTPException(
            status_code=401, detail="Mauvais email ou mot de passe"
        )

    return schemas.User.from_orm(user)


async def delete_current_user(
    db: _orm.Session = fastapi.Depends(get_db),
    token: str = fastapi.Depends(oauth2schema),
):
    try:
        payload = jwtt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = db.query(models.User).get(payload["id"])
        db.delete(user)
        db.commit()

    except:
        raise fastapi.HTTPException(
            status_code=401, detail="Problème lors de la supprésion"
        )

    return schemas.User.from_orm(user)


def get_items(db:  _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(item: schemas.ItemCreate, db:  _orm.Session):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def contact_create(contact: schemas.ContactCreate,
                   db: _orm.Session,
                   token: str = fastapi.Depends(oauth2schema),
                   ):

    payload = jwtt.decode(token, JWT_SECRET, algorithms=["HS256"])
    user = db.query(models.User).get(payload["id"])
    db_contact = models.Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


def get_contact(db:  _orm.Session, skip: int = 0, limit: int = 10):
    return db.query(models.Contact).offset(skip).limit(limit).all()


def get_services(db:  _orm.Session, skip: int = 0, limit: int = 10):
    return db.query(models.Services).offset(skip).limit(limit).all()


def create_services(services: schemas.ServiceCreate, db:  _orm.Session):
    db_services = models.Services(**services.dict())
    db.add(db_services)
    db.commit()
    db.refresh(db_services)
    return db_services


def create_chatbox(chatbox: schemas.ChatboxCreate, db: _orm.Session):
    db_chatbox = models.Chatbox(**chatbox.dict())
    db.add(db_chatbox)
    db.commit()
    db.refresh(db_chatbox)
    return db_chatbox


def read_chatbox(db:  _orm.Session, skip: int = 0, limit: int = 10):
    return db.query(models.Chatbox).offset(skip).limit(limit).all()


def create_devis(devis: schemas.DevisCreate, db: _orm.Session):
    db_devis = models.Devis(**devis.dict())
    db.add(db_devis)
    db.commit()
    db.refresh(db_devis)
    return db_devis


def read_devis(db:  _orm.Session, skip: int = 0, limit: int = 10):
    return db.query(models.Devis).offset(skip).limit(limit).all()


def create_facture(facture: schemas.FactureCreate, db: _orm.Session):
    db_facture = models.Facture(**facture.dict())
    db.add(db_facture)
    db.commit()
    db.refresh(db_facture)
    return db_facture


def read_facture(db:  _orm.Session, skip: int = 0, limit: int = 10):
    return db.query(models.Facture).offset(skip).limit(limit).all()
