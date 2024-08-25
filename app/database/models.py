from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class DataEntry( Base ):
    __tablename__ = "data_entries"

    id = Column( Integer, primary_key = True, index = True )
    content = Column( String )
    timestamp = Column( DateTime )
