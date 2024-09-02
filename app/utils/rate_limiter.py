import asyncio
import time
from fastapi import HTTPException

class RateLimiter:
    def __init__( self, rate_limit: int = 100, per: int = 120 ):
        self.rate_limit = rate_limit
        self.per = per
        self.tokens = rate_limit
        self.updated_at = time.monotonic()
        self.lock = asyncio.Lock()

    async def acquire( self ):
        async with self.lock:
            now = time.monotonic()
            time_passed = now - self.updated_at
            self.tokens += time_passed * ( self.rate_limit / self.per )
            if self.tokens > self.rate_limit:
                self.tokens = self.rate_limit
            self.updated_at = now

            if self.tokens < 1:
                wait_time = ( 1 - self.tokens ) * ( self.per / self.rate_limit )
                raise HTTPException( status_code = 429, detail = f"Rate limit exceeded. Please try again in {wait_time:.2f} seconds.")

            self.tokens -= 1

    async def wait( self ):
        while True:
            try:
                await self.acquire()
                break
            except HTTPException as e:
                if e.status_code == 429:
                    wait_time = float( e.detail.split()[-2] )
                    await asyncio.sleep( wait_time )
                else:
                    raise

rate_limiter = RateLimiter()
