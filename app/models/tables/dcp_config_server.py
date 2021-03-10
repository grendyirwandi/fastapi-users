from app.core.ConnectionDb import ConnectionDb
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

class dcp_config_server(ConnectionDb().Base):
    __tablename__ = "dcp_config_server"

    id = Column(Integer, primary_key=True)
    id_customer = Column(Integer)
    subdomain = Column(String(25))
    user_db = Column(String(25))
    password_db = Column(String(255))
    name_db = Column(String(25))
    status_user_db = Column(Integer)
    status_subdomain = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)