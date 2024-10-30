from typing import Any

from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL

engine: Engine = create_engine(DATABASE_URL)
Base: Any = declarative_base()
Session = sessionmaker(engine)
