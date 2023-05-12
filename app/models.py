from sqlalchemy import Column, INTEGER, VARCHAR, BOOLEAN, TIMESTAMP, TEXT, ForeignKey, text
from .database import Base, engine

class PartTable(Base):
    __tablename__='part_tb'
    pid = Column(INTEGER, autoincrement=True, primary_key=True, nullable=False) 
    part_name = Column(VARCHAR(100), nullable=False)
    mat_comp = Column(VARCHAR(100), nullable=False)
    age = Column(INTEGER, nullable=False)
    condition = Column(BOOLEAN, nullable=False)
    location = Column(VARCHAR(100), nullable=False)
    manufacturer = Column(VARCHAR(100), nullable=False)
    aircraft_mod = Column(VARCHAR(100), nullable=False)

class SustainData(Base):
    __tablename__='sustain_data'
    sid = Column(INTEGER,ForeignKey('part_tb.pid', ondelete='CASCADE'), primary_key=True, nullable=False)
    pot_usecase = Column(VARCHAR(255), nullable=False)
    remanufacPotential = Column(INTEGER, nullable=False)
    lca = Column(INTEGER, nullable=False)

class RecycleData(Base):
    __tablename__='recycle_data'
    sid = Column(INTEGER, ForeignKey('sustain_data.sid', ondelete='CASCADE'), primary_key=True, nullable=False)
    rCarbonFP = Column(INTEGER, nullable=False)
    rWaterUsage = Column(INTEGER, nullable=False)
    rLandFill = Column(INTEGER, nullable=False)
    rEneConsum = Column(INTEGER, nullable=False)
    rToxicScore = Column(INTEGER, nullable=False)

class NewManuData(Base):
    __tablename__='New_manu_data'
    sid = Column(INTEGER, ForeignKey('sustain_data.sid', ondelete='CASCADE'), primary_key=True, nullable=False)
    nCarbonFP = Column(INTEGER, nullable=False)
    nWaterUsage = Column(INTEGER, nullable=False)
    nLandFill = Column(INTEGER, nullable=False)
    nEneConsum = Column(INTEGER, nullable=False)
    nToxicScore = Column(INTEGER, nullable=False)

class Manufacturer(Base):
    __tablename__ = 'manufacturer'
    user_id = Column(VARCHAR(100), primary_key=True, nullable=False)
    pwd = Column(VARCHAR(100), nullable=False)
    company = Column(VARCHAR(100), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('NOW()'))

class Airline(Base):
    __tablename__ = 'airline'
    user_id = Column(VARCHAR(100), primary_key=True, nullable=False)
    pwd = Column(VARCHAR(100), nullable=False)
    company = Column(VARCHAR(100), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('NOW()'))

class RFacility(Base):
    __tablename__ = 'rfacility'
    user_id = Column(VARCHAR(100), primary_key=True, nullable=False)
    pwd = Column(VARCHAR(100), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('NOW()'))


Base.metadata.create_all(bind=engine)