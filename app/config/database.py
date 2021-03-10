from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only
import os
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

db = {
    "hostname": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "username": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "database": os.getenv("DB_NAME"),
    "dbdriver": "mysql"
}
