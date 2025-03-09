"""
Not used in the current version of the project.
"""

import sys
import pathlib

from supabase import Client, create_client
from supabase._async.client import AsyncClient, create_client as acreate_client

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from config import settings


class SuperbaseClient:
    """
    Service Role AClient for Supabase
    """

    _instance = None

    @classmethod
    async def get_instance(cls) -> AsyncClient:
        if cls._instance is None:
            url = settings.SUPABASE_URL
            key = settings.SUPABASE_SERVICE_ROLE_KEY
            cls._instance = await acreate_client(url, key)
        return cls._instance


class SuperbaseSyncClient:
    """
    Service Role Client for Supabase
    """

    _instance = None

    @classmethod
    def get_instance(cls) -> Client:
        if cls._instance is None:
            url = settings.SUPABASE_URL
            key = settings.SUPABASE_SERVICE_ROLE_KEY
            cls._instance = create_client(url, key)
        return cls._instance
