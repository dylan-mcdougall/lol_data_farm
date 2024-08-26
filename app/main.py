from fastapi import FastAPI as fa
from .matches.router import router as matches_router
from .database.router import router as database_router
from .accounts.router import router as accounts_router

app = fa()

app.include_router( matches_router, prefix = "/matches", tags = [ "matches" ] )
app.include_router( database_router, prefix = "/database", tags = [ "database" ] )
app.include_router( accounts_router, prefix = "/accounts", tags = [ "accounts" ] )

@app.get( "/" )
def read_root():
    
    return { "Hello": "World" }

# @app.get( "/items/{item_id}" )
# def read_item( item_id: int, q: Union[ str, None ] = None ):
#     return { "item_id": item_id, "q": q }
