from fastapi import APIRouter, HTTPException
from .service import matches_service

router = APIRouter()

@router.get("/fetch")
async def fetch_matches():
    try:
        data = await matches_service.fetch_data()
        return { "message": "Data fetched successfully", "data": data }
    except Exception as e:
        raise HTTPException( status_code = 500, detail = str( e ) )
    

