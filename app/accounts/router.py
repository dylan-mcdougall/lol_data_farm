from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from .service import accounts_service
from ..database.service import DatabaseService
from datetime import datetime, timedelta

router = APIRouter()

last_fetch_time = None

async def fetch_Accounts( db: Session ):
    global last_fetch_time
    database_service = DatabaseService( db )

    try:
        data = await accounts_service.fetch_accounts()
        
        for account in data.get("accounts", []):
            database_service.store_data( str( account ) )

        last_fetch_time = datetime.utcnow()

    except Exception as e:
        print( f"Error fetching and storing accounts: { str( e ) }" )

@router.post( "/fetch" )
async def fetch_accounts( background_tasks: BackgroundTasks, db: Session = Depends( get_db ) ):
    global last_fetch_time

    if last_fetch_time is None or datetime.utcnow() - last_fetch_time > timedelta( hours = 24 ):
        background_tasks.add_task( fetch_accounts, db )
        return { "message": "Account fetch scheduled" }
    
    else:
        return { "message": "Account fetch skipped, last fetch was less than 24 hours ago" }

@router.get( "/list" )
async def list_accounts(db: Session = Depends( get_db ) ):
    database_service = DatabaseService( db )
    accounts = database_service.get_all_data()

    return { "accounts": accounts }
