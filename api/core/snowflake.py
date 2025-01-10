from typing import Annotated, List
from fastapi import Depends
from snowflake.connector import DictCursor, connect
from snowflake.connector.cursor import SnowflakeCursor

from api.core.cache import cachefunc, redis_client
from api.config import settings


class Snowflake:
    def __init__(self, 
                 user: str,
                 password: str,
                 account: str,
                 database: str,
                 warehouse: str,
                 ):
        self._user = user
        self._password = password
        self._account = account
        self._database = database
        self._warehouse = warehouse
        
        self._authed = False
        self._conn = None
        
    def __exit__(self, exc_type, exc_value, traceback):
        self._conn.close()

    async def _auth(self):
        if not self._authed:
            self._conn = connect(
                user=self._user,
                password=self._password,
                account=self._account,
                warehouse=self._warehouse,
                database=self._database
            )
            self._authed = True
            
        return
    
    @cachefunc(r=redis_client, skip_self=True)
    async def fetchall(self, query: str, 
                             params: dict = None) -> List[dict] | List[tuple]:
        await self._auth()
        
        cursor = self._conn.cursor(DictCursor)
        cursor.execute(query, params)
            
        return cursor.fetchall()
    
async def get_snowflake() -> Snowflake:
    sf = Snowflake(
        user=settings.snowflake_user,
        password=settings.snowflake_password,
        account=settings.snowflake_account,
        database=settings.snowflake_database,
        warehouse=settings.snowflake_warehouse
    )
    return sf

SnowflakeConn = Annotated[Snowflake, Depends(get_snowflake)]