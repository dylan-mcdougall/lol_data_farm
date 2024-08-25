import asyncio
from typing import Dict, Any

class RateLimiter:
    def __init__( self, rate_limit: int, time_period: int ):
        self.rate_limit = rate_limit
        self.time_period = time_period
        self.tokens = rate_limit
        self.last_refill = asyncio.get_event_loop().time()

    async def acquire( self ):
        while True:
            current_time = asyncio.get_event_loop.time()
            time_passed = current_time - self.last_refill
            new_tokens = int( time_passed * ( self.rate_limit / self.time_period ) )

            if new_tokens > 0:
                self.tokens = min( self.rate_limit, self.tokens + new_tokens )
                self.last_refill = current_time

            if self.tokens > 0:
                self.tokens -= 1
                return
            
            await asyncio.sleep( 0.1 )

class MatchesService:
    def __init__( self ):
        self.rate_limiter = RateLimiter( rate_limit = 100, time_period = 100 * 60 )

    async def fetch_data( self ) -> Dict[ str, Any ]:
        await self.rate_limiter.acquire()

        await asyncio.sleep(1)
        return { "data": "Sample data" }
    
matches_service = MatchesService()
