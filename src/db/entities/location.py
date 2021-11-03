# -*- coding: utf-8 -*-
from datetime import datetime

from geoalchemy2 import Geometry
from sqlalchemy import Column, DateTime, Integer, String

from src.db.entities.base import Base


class Location(Base):
    __tablename__ = "location"
    __table_args__ = {"schema": "geo"}

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_date = Column(DateTime(timezone=True), default=datetime.utcnow())
    extent = Column(Geometry(geometry_type="POLYGON", srid=4326))
