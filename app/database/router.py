from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .service import DatabaseService
from ..dependencies import get_db

router = APIRouter()

@router.post( "/store" )
async def store_data( content: str, db: Session = Depends( get_db ) ):
    try:
        service = DatabaseService( db )
        entry = service.store_data( content )
        return { "message": "Data stored successfully", "id": entry.id }
    except Exception as e:
        raise HTTPException( status_code = 500, detail = str( e ) )
    
router.get( "/query" )
async def query_data( db: Session = Depends( get_db ) ):
    try:
        service = DatabaseService( db )
        data = service.get_all_data()
        return { "data": [ { "id": entry.id, "content": entry.content, "timestamp": entry.timestamp } for entry in data ] }
    except Exception as e:
        raise HTTPException( status_code = 500, detail = str( e ) )
