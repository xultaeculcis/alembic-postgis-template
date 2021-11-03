# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import src.config as config

engine = create_engine(config.DATABASE_URI, pool_pre_ping=True, echo=True)


# Create a local session maker to interact with the db via ORM
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
