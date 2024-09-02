import asyncio
import aiohttp
from fastapi import Depends
from ..config import Settings, get_settings
from ..utils.rate_limiter import rate_limiter
from ..utils.queue_manager import queue_manager

class AccountsService:
    TIERS = ['challenger']
    REGIONS = ['na1']

    def __init__( self ):
        pass

    @staticmethod
    async def fetch_tier( self, region: str, tier: str, settings: Settings = Depends( get_settings ) ):
        await rate_limiter.wait()
        async with aiohttp.ClientSession() as session:
            url = f"https://{region}.api.riotgames.com/lol/league/v4/{tier}leagues/by-queue/RANKED_SOLO_5x5?api_key={settings.API_KEY}"
            async with session.get( url ) as response:
                data = await response.json()
                await self.process_data( data, region, tier )
    
    @staticmethod
    async def process_tier_data( self, data, region: str, tier: str ):
        processed_data = self.process_data( data )
        pass
    
    @staticmethod
    def process_data( self, data ):
        pass

    @staticmethod
    def schedule_fetch_job():
        for region in AccountsService.REGIONS:
            for tier in AccountsService.TIERS:
                queue_manager.schedule_job(
                    AccountsService.fetch_tier,
                    args = ( region, tier ),
                    interval = 86400,
                    repeat = None
                )

accounts_service = AccountsService()
