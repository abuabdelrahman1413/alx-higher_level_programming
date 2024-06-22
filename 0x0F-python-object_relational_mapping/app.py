import sys
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

eng = create_engine('mysql+mysqldb://root:1413@localhost:3306/hbtn_0e_0_usa?charset=utf8', echo=True)
# eng.connect()

# print(eng)
Base = declarative_base()
class User(Base):
  __tablename__ = 'users'
  id = Column(Integer(), primary_key=True)
  name = Column(String(128), nullable=False)


Base.metadata.create_all(bind=eng)
