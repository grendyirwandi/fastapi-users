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
    "hostname": os.getenv("CACHE_HOST"),
    "port": os.getenv("CACHE_PORT"),
    "password": "",
    "database": os.getenv("CACHE_DB")
}
