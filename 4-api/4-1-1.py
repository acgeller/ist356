import requests
import dotenv
import os
dotenv.load_dotenv()

CENT_API_KEY = os.getenv("CENT_API_KEY")
USERNAME = os.getenv("USERNAME")