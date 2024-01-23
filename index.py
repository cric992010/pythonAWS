import os
from dotenv import load_dotenv

load_dotenv(".env")

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

print(client_id)
print(client_secret)