import requests

from APIRateLimiter import APIRateLimiter
from RoutingValues import RoutingValues


class ApiClient:
    def __init__(self, platform_value: str, regional_value: str, rate_limiter: APIRateLimiter):
        self.rate_limiter = rate_limiter
        self.api_token_header = {
            "X-Riot-Token": "<MY_DEVELOPER_TOKEN>"
        }
        RoutingValues.initialize()
        self.platform_url_base = RoutingValues.PLATFORM_ROUTING_VALUES.get(platform_value)
        self.regional_url_base = RoutingValues.REGIONAL_ROUTING_VALUES.get(regional_value)

    def get_platform_url(self):
        return f"https://{self.platform_url_base}"

    def get_regional_url(self):
        return f"https://{self.regional_url_base}"

    def perform_request(self, url: str, params: dict = None, headers: dict = None):
        if headers is None:
            headers = dict()
        headers.update(self.api_token_header)
        routing_value = RoutingValues.extract_routing_value(url)
        try:
            if not self.rate_limiter.allow_request(routing_value):
                raise requests.exceptions.RequestException(f"API rate limit reached for {url}")
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(
                f"Error performing request: {str(e)}"
            ) from e

    def fetch_ranked_players(self, queue: str, tier: str, division: str, page: int = 1):
        url = f"{self.get_platform_url()}/lol/league-exp/v4/entries/{queue}/{tier}/{division}"
        return self.perform_request(url, params={"page": page})

    def fetch_summoner_puuid(self, summoner_id: str):
        url = f"{self.get_platform_url()}/lol/summoner/v4/summoners/{summoner_id}"
        response = self.perform_request(url)
        return response.get("puuid")

    def fetch_account(self, puuid: str):
        url = f"{self.get_regional_url()}/riot/account/v1/accounts/by-puuid/{puuid}"
        return self.perform_request(url)

    def fetch_matches_ids(self, puuid: str, type: str, count: int = 50, start: int = 0):
        url = f"{self.get_regional_url()}/lol/match/v5/matches/by-puuid/{puuid}/ids"
        return self.perform_request(url, params={"type": type, "count": count, "start": start})

    def fetch_match_data(self, match_id: str):
        url = f"{self.get_regional_url()}/lol/match/v5/matches/{match_id}"
        return self.perform_request(url)
