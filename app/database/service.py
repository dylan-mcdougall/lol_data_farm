from sqlalchemy.orm import Session
from .models import DataEntry, Account
from datetime import datetime

class DatabaseService:
    def __init__( self, db: Session ):
        self.db = db

    def store_data( self, content: str ):
        new_entry = DataEntry( content = content, timestamp = datetime.utcnow() )
        self.db.add( new_entry )
        self.db.commit()
        self.db.refresh( new_entry )
        return new_entry
    
    def get_all_data( self ):
        return self.db.query( DataEntry ).all()
    
    def store_account( self, account_data: dict ):
        new_account = Account( **account_data )
        self.db.add( new_account )
        self.db.commit()
        self.db.refresh( new_account )
        return new_account
    
    def get_all_accounts( self ):
        return self.db.query( Account ).all()
    
    def get_account_by_summoner_id( self, summoner_id: str ):
        return self.db.query( Account ).filter( Account.summoner_id == summoner_id ).first()
    
    def update_account( self, summoner_id: str, account_data: dict ):
        account = self.get_account_by_summoner_id( summoner_id )

        if account:
            for key, value in account_data.items():
                setattr( account, key, value )

            self.db.commit()
            self.db.refresh( account )
        return account
