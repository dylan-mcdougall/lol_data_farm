import httpx
from ..config import Settings, get_settings
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
            existing_account = database_service.get_account_by_summoner_id( account[ "summoner_id" ] )
            
            if existing_account:
                database_service.update_account( account[ "summoner_id" ], account )
            else:
                database_service.store_account( account )

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

@router.get( "/kr/masters" )
async def get_kr_masters( settings: Settings = Depends( get_settings )):
    url = f"https://kr.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5?api_key={settings.API_KEY}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"There are {len(data["entries"])} players in the MASTERS tier in KR.")
        return data
    
    else:
        return {"error": "Failed to fetch data from RGAPI"}
    
@router.get( "/na/masters" )
async def get_na_masters( settings: Settings = Depends( get_settings )):
    url = f"https://na1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5?api_key={settings.API_KEY}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"There are {len(data["entries"])} players in the MASTERS tier in NA.")
        return data
    
    else:
        return {"error": "Failed to fetch data from RGAPI"}

@router.get( "/list" )
async def list_accounts( db: Session = Depends( get_db ) ):
    database_service = DatabaseService( db )
    accounts = database_service.get_all_accounts()

    return { "accounts": [ account.__dict__ for account in accounts ] }
