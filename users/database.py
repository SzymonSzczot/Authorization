import json

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


secrets = json.loads(open("secrets.json", "r").read())
SQLALCHEMY_DATABASE_URL = f"postgresql://{secrets['DB_USER']}:{secrets['DB_PASSWORD']}@localhost:5432/auth"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BaseModel = declarative_base()
