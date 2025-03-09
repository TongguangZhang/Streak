import sys
import pathlib
from typing import Annotated

from supabase import AClient
from fastapi import Depends

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from database import supabase_client

SupabaseDep = Annotated[AClient, Depends(supabase_client.SuperbaseClient.get_instance())]
