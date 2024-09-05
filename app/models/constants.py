import os

from dotenv import load_dotenv

# Load the .env file
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=ENV_PATH)

# API_KEY = os.getenv("API_KEY", "")
