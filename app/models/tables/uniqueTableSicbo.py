from app.core.ConnectionDb import ConnectionDb
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

class uniqueTableSicbo(ConnectionDb().Base):
    __tablename__ = "uniqueTableSicbo"

    id = Column(Integer, primary_key=True)
    authId = Column(Integer)
    tableType = Column(String(25))
    key = Column(String(255))
    tableName = Column(String(255))
    logo = Column(String(255))
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)