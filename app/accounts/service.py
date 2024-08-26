import asyncio
from typing import Dict, Any

class AccountsService:
    async def fetch_accounts(self) -> Dict[str, Any]:

        await asyncio.sleep(1)
        return {
            "accounts": [
                {
                    "tier": "DIAMOND",
                    "summoner_id": "abcd1234",
                    "leaguePoints": 75,
                    "rank": "II",
                    "wins": 120,
                    "losses": 100,
                    "inactive": False
                },
                {
                    "tier": "PLATINUM",
                    "summoner_id": "efgh5678",
                    "leaguePoints": 50,
                    "rank": "III",
                    "wins": 80,
                    "losses": 70,
                    "inactive": False
                }
            ]
        }
        
accounts_service = AccountsService()
