from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .database import Base

class DataEntry( Base ):
    __tablename__ = "data_entries"

    id = Column( Integer, primary_key = True, index = True )
    content = Column( String )
    timestamp = Column( DateTime )

class Account( Base ):
    __tablename__ = "accounts"

    id = Column( Integer, primary_key=True, index=True )
    tier = Column( String )
    summoner_id = Column( String, unique=True, index=True )
    leaguePoints = Column( Integer )
    rank = Column( String )
    wins = Column( Integer )
    losses = Column( Integer )
    inactive = Column( Boolean )

    def __repr__( self ):
        return f"<Account( id={self.id}, tier='{self.tier}', summoner_id='{self.summoner_id}', rank='{self.rank}' )>"
