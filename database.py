from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://cgsukvjjfzlgrd:e980af14f1b9a825d213103d365bb33daeee148528d94274a2f3c8181ca81bec@ec2-52-30-67-143.eu-west-1.compute.amazonaws.com:5432/demsi71c8nc1no"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
