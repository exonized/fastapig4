import databases
import sqlalchemy


DATABASE_URL = "postgresql://cgsukvjjfzlgrd:e980af14f1b9a825d213103d365bb33daeee148528d94274a2f3c8181ca81bec@ec2-52-30-67-143.eu-west-1.compute.amazonaws.com:5432/demsi71c8nc1no"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL
)