import logging
import os

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

log_format = logging.Formatter("%(asctime)s : %(levelname)s - %(message)s")

# root logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# standard stream handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_format)
root_logger.addHandler(stream_handler)

load_dotenv()


class Settings(BaseSettings):
    SUPABASE_URL: str = Field(default_factory=lambda: os.getenv("SUPABASE_URL"))
    SUPABASE_ANON_KEY: str = Field(default_factory=lambda: os.getenv("SUPABASE_ANON_KEY"))
    SUPABASE_SERVICE_ROLE_KEY: str = Field(default_factory=lambda: os.getenv("SUPABASE_SERVICE_ROLE_KEY"))


settings = Settings()
