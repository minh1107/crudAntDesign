from sqlalchemy import Column, Integer, String
from app.db.session import Base

class AuthUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    username = Column(String, index=True, unique=True)
    email = Column(String, index=True, unique=True)
    phone = Column(String, index=True)
    website = Column(String)
    addressstreet = Column(String)
    addresssuite = Column(String)
    addresscity = Column(String)
    addresszipcode = Column(String)
    companyname = Column(String)
    companycatchphrase = Column(String)
    companybs = Column(String)