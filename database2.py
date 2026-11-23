from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase
DATABASE_URL = "postgresql+psycopg://postgres:Abhi%402733@host.docker.internal:5432/fantastic"

engine=create_engine(DATABASE_URL)

sessionlocal=sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

