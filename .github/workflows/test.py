from dotenv import load_dotenv
import os

load_dotenv()  # load from .env if available


url = os.getenv("URL")

print(f"URL: {url}")