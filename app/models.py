from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String
from .database import Base

class Warehouse(Base):
    __tablename__ = "warehouses"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # This stores the boundary of the warehouse/route
    geom = Column(Geometry('POLYGON', srid=4326))

