from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .database import Base

class DataEntry( Base ):
    __tablename__ = "data_entries"

    id = Column( Integer, primary_key = True, index = True )
    content = Column( String )
    timestamp = Column( DateTime )

class Account( Base ):
    __tablename__ = "accounts"

    id = Column( Integer, primary_key = True, index = True )
    region = Column ( String, index = True )
    tier = Column( String )
    summoner_id = Column( String, index = True )
    account_id = Column( String, index = True )
    puuid = Column( String, unique = True, index = True )
    league_points = Column( Integer )
    rank = Column( String )
    wins = Column( Integer )
    losses = Column( Integer )
    inactive = Column( Boolean )

class Match( Base ):
    __tablename__ = "matches"

    id = Column( Integer, primary_key = True, index = True )

class Champion( Base ):
    __tablename__ = "champions"

    id = Column( Integer, primary_key = True, index = True )


    def __repr__( self ):
        return f"<Account( id={self.id}, tier='{self.tier}', summoner_id='{self.summoner_id}', rank='{self.rank}' )>"
