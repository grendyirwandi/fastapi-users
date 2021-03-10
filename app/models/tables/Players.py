from app.core.ConnectionDb import ConnectionDb
from sqlalchemy.ext.declarative import declarative_base
import enum
from sqlalchemy import Table, Column, String, Integer, Float, DateTime, Enum, MetaData


class Badge(enum.Enum):
    one = 'standard'
    two = 'gold'

class Players():
    __metadata = MetaData()
    users = Table('players', __metadata,
        Column('id', Integer, primary_key=True),
        Column('userId', Integer),
        Column('authId', Integer),
        Column('displayName', String(255)),
        Column('balance', Float),
        Column('currency', String(255)),
        Column('badge', Enum(Badge)),
        Column('createdAt', DateTime),
        Column('updatedAt', DateTime)
    )
    # __tablename__ = "players"

    # id = Column(Integer, primary_key=True)
    # userId = Column(Integer)
    # authId = Column(Integer)
    # displayName = Column(String(255))
    # balance = Column(Float)
    # currency = Column(String(255))
    # badge = Column(Enum(Badge))
    # createdAt = Column(DateTime)
    # updatedAt = Column(DateTime)