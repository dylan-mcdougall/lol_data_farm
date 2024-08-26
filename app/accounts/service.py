import asyncio
from typing import Dict, Any

class AccountsService:
    async def fetch_accounts( self ) -> Dict[ str, Any ]:
        await asyncio.sleep(1)
        
        return {
            "accounts": [
                { "id": "1" }
            ]
        }
        
accounts_service = AccountsService()
