  
import os
from datetime import datetime

from app.db import Base, engine

from sqlalchemy import Column, Integer, String, Text, text, DATETIME

class User(Base):
  __tablename__ = 'users'

  id = Column('id', Integer, primary_key = True)
  name = Column('name', String(32))
  time = Column('time', DATETIME)

  def __repr__(self):
    return '<User id={id} name={name} time={time!r}>'.format(
      id=self.id, name=self.name, time=self.time
    )
