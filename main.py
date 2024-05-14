from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client

# Load Token from .env
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

# Intents

intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)

# Startup

@client.event
async def on_ready() -> None:
  print("Logged in as {client.user}")

# Entry Point

def main() -> None:
  client.run(token=TOKEN)

if __name__ = "__main__":
  main()
