import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from server.database import supabase_client

supabase = supabase_client.SuperbaseSyncClient.get_instance()
