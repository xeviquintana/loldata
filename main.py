from APIClient import ApiClient
from APIRateLimiter import APIRateLimiter

"""
RIOT API endpoints

1. Summoner API
2. Match API
3. Champion Mastery API
4. Champion API
5. League API
6. Spectator API
7. Static Data API (via Data Dragon)
8. Status API
9. Third-Party Code API
"""


def init_europe_west_api_client(rate_limiter: APIRateLimiter):
    return ApiClient("euw1", "europe", rate_limiter)


def init_north_america_api_client(rate_limiter: APIRateLimiter):
    return ApiClient("na1", "americas", rate_limiter)


def main():
    # euw_api_client = init_europe_west_api_client(APIRateLimiter.with_default_limits())
    na_api_client = init_north_america_api_client(APIRateLimiter.with_default_limits())
    ranked_players = na_api_client.fetch_ranked_players("RANKED_SOLO_5x5", "CHALLENGER", "I")
    summoners = []
    processed_matches_ids = set()
    champs_played = {}
    top_players = 5
    for i, player in enumerate(sorted(ranked_players, key=lambda x: x.get('leaguePoints'), reverse=True)[:top_players],
                               start=1):
        puuid = na_api_client.fetch_summoner_puuid(player.get("summonerId"))
        summoner = player | {"puuid": puuid}
        account_data = na_api_client.fetch_account(puuid)
        summoner |= account_data
        summoners.append(summoner)
        print(f"Rank {i}: {summoner.get("gameName")}#{summoner.get("tagLine")}")
        match_ids = na_api_client.fetch_matches_ids(puuid, "ranked", 10)
        for match_id in match_ids:
            if match_id in processed_matches_ids:
                continue
            match_data = na_api_client.fetch_match_data(match_id)
            for participant in match_data.get("metadata").get("participants"):
                try:
                    champion = match_data.get("info").get("participants")[i].get("championName")  # should be championId
                    champs_played[champion] = champs_played.get(champion, 0) + 1
                except (KeyError, IndexError) as e:
                    raise RuntimeError(
                        f"Error getting champion for participant {participant} in game {match_id}: {str(e)}"
                    ) from e
            processed_matches_ids.add(match_id)

    top_champs = 10
    print(f"Top {top_champs} champions played:")
    for champion, count in sorted(champs_played.items(), key=lambda x: x[1], reverse=True)[:top_champs]:
        print(f"  {champion} - {count} occurrences")


if __name__ == "__main__":
    main()
