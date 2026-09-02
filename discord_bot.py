import requests
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

bot_token = os.environ["DISCORD_TOKEN"]
discord_application_id = os.environ["APPLICATION_ID"]
discord_user_id = os.environ["USER_ID"]

url = (
    f"https://discord.com/api/v9/applications/"
    f"{discord_application_id}/users/"
    f"{discord_user_id}/identities/0/profile"
)
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bot {bot_token}",
    "User-Agent": "DiscordBot (https://github.com/discord/discord-api-docs, 1.0.0)",
}

def update_dc(new_json):
	response = requests.patch(
	    url,
	    headers=headers,
	    json=new_json,
	)
	print("Status:", response.status_code)
	print(response.text)
