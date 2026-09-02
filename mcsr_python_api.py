import requests
import math
from datetime import datetime

img_start = "https://github.com/tatefritz/MCSR-Ranked/blob/main/rank_icons/"
img_end = ".png?raw=true"
USERNAME = "Tatertot5"
ELO_RANGES = [
	(0, 399, ["Coal I", f"{img_start}coal_I{img_end}"]),
	(400, 499, ["Coal II", f"{img_start}coal_II{img_end}"]),
	(500, 599, ["Coal III", f"{img_start}coal_III{img_end}"]),
	(600, 699, ["Iron I", f"{img_start}iron_I{img_end}"]),
	(700, 799, ["Iron II", f"{img_start}iron_II{img_end}"]),
	(800, 899, ["Iron III", f"{img_start}iron_III{img_end}"]),
	(900, 999, ["Gold I", f"{img_start}gold_I{img_end}"]),
	(1000, 1099, ["Gold II", f"{img_start}gold_II{img_end}"]),
	(1100, 1199, ["Gold III", f"{img_start}gold_III{img_end}"]),
	(1200, 1299, ["Emerald I", f"{img_start}emerald_I{img_end}"]),
	(1300, 1399, ["Emerald II", f"{img_start}emerald_II{img_end}"]),
	(1400, 1499, ["Emerald III", f"{img_start}emerald_III{img_end}"]),
	(1500, 1649, ["Diamond I", f"{img_start}diamond_I{img_end}"]),
	(1650, 1799, ["Diamond II", f"{img_start}diamond_II{img_end}"]),
	(1800, 1999, ["Diamond III", f"{img_start}diamond_III{img_end}"]),
	(2000, 3000, ["Netherite", f"{img_start}netherite{img_end}"]),
	(-1, -1, ["Unranked", f"{img_start}unranked{img_end}"]),
]

def format_ms(milli: int) -> str:
	minutes = (milli // (1000 * 60)) % 60
	hours = (milli // (1000 * 60 * 60)) % 24
	days = milli // (1000 * 60 * 60 * 24)

	if days:
		return f"{days}d {hours}h {minutes}m"
	return f"{hours}h {minutes}m"

def format_time(time: int) -> str:
	if time == None:
		return "0h 00m"
	ms = time % 1000
	seconds = (time // 1000) % 60
	minutes = (time // (1000 * 60)) % 60
	hours = time // (1000 * 60 * 60)
	if hours > 0:
		return f"{hours}:{minutes:02}:{seconds:02}.{ms:03}"
	return f"{minutes:02}:{seconds:02}.{ms:03}"

def get_rank(elo) -> list:
	if elo == None:
		return ELO_RANGES[16][2]
	for low, high, result in ELO_RANGES:
		if low <= elo <= high:
			return result
	raise ValueError("Score out of range")

def get_info(username: str) -> dict:
	URL = f'https://api.mcsrranked.com/users/{username}'
	response = requests.get(URL)
	if response.status_code == 200:
		data = response.json()["data"]
	else:
		print(response.status_code)

	print(data)
	season_stats = data["statistics"]["season"]
	wins = season_stats["wins"]["ranked"]
	loses = season_stats["loses"]["ranked"]
	elo = data["seasonResult"]["last"]["eloRate"]
	badge = get_rank(elo)

	return {
		'username': username,
		'head_image': f'https://mc-heads.net/head/{data["uuid"]}/100/left/',
		'badge_type': badge[0],
		'badge_image': badge[1],
		'elo': elo,
		'rank_placement': data["seasonResult"]["last"]["eloRank"],
		'peak_elo': data["seasonResult"]["highest"],
		'wins': wins,
		'winrate': (str(math.floor((wins/(wins+loses))*100))+"%") if (wins+loses) > 0 else "0%",
		'played_matches': season_stats["playedMatches"]["ranked"],
		'personal_best': format_time(data["statistics"]["total"]["bestTime"]["ranked"]),
		'play_time': format_ms(season_stats["playtime"]["ranked"]),
		'last_played': datetime.fromtimestamp(data["timestamp"]["lastRanked"]).strftime("%m/%d/%Y"),
	}

def main():
	get_info(USERNAME)
	#print(get_info(USERNAME))


if __name__ == '__main__':
	main()