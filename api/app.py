from fastapi import FastAPI

from api.core.snowflake import SnowflakeConn
from version import __version__

app = FastAPI()

@app.get("/")
async def read_root(sf: SnowflakeConn):
    """
    Example route to demonstrate there is no delay
    on depency injection if not needed
    """
    return {"Hello": "World"}

@app.get("/login")
async def login(sf: SnowflakeConn):
    """
    Example route to demonstrate the dependency injection
    of the Snowflake connection when it only needs to authenticate
    """
    await sf._auth()
    return {"status": "ok"}

@app.get('/cache')
async def this_gets_cached(sf: SnowflakeConn):
    """
    Example route to demonstrate the dependency injection
    of the Snowflake connection when it only needs to authenticate
    """
    data = await sf.fetchall('SELECT CURRENT_TIMESTAMP()')
    return {"data": data}



@app.get("/health")
async def health():
    return {"status": "ok", "version": __version__}