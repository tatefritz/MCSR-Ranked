from mcsr_python_api import get_info
from discord_bot import update_dc

MC_USERNAME = "Tatertot5"

def convert_data(data) -> dict:
	return {
	"username": f"{MC_USERNAME}",
	"data": {
		"dynamic": [
			{
				"type": 3,
				"name": "head",
				"value": {
					"url": f"{data["head_image"]}"
				}
			},
			{
				"type": 1,
				"name": "badge_type",
				"value": f"{data["badge_type"]}"
			},
			{
				"type": 3,
				"name": "badge_image",
				"value": {
					"url": f"{data["badge_image"]}"
				}
			},
			{
				"type": 1,
				"name": "elo",
				"value": f"{data["elo"]} Elo "
			},
			{
				"type": 1,
				"name": "placement",
				"value": f"#{data["rank_placement"]}"
			},
			{
				"type": 1,
				"name": "personal_best",
				"value": f"{data["personal_best"]}"
			},
			{
				"type": 1,
				"name": "winrate",
				"value": f"{data["winrate"]}"
			},
			{
				"type": 1,
				"name": "wins",
				"value": f"{data["wins"]}"
			},
			{
				"type": 1,
				"name": "peak_elo",
				"value": f"{data["peak_elo"]}"
			},
			{
				"type": 1,
				"name": "last_played",
				"value": f"{data["last_played"]}"
			},
			{
				"type": 1,
				"name": "playtime",
				"value": f"{data["play_time"]}"
			},
			{
				"type": 1,
				"name": "matches",
				"value": f"{data["played_matches"]}"
			}
		]
	}
}

def main() -> None:
	try:
		data = get_info(MC_USERNAME)
		discord_formatted_data = convert_data(data)
		update_dc(discord_formatted_data)
	except:
		pass




if __name__ == '__main__':
	main()