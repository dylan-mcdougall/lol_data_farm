from sqlalchemy.orm import Session
from .models import DataEntry
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
    
