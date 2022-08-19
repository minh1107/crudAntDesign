from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.db.session import Base

# tạo 1 alchemy để kết nối với dbbase
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