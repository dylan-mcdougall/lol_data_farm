import uvicorn
from app.database.database import engine
from app.database.models import Base

Base.metadata.create_all( bind = engine )

if __name__ == "__main__":
    uvicorn.run( "app.main:app", host="localhost", port=8000, reload=True )
