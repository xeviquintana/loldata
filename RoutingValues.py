import re


class RoutingValues:
    PLATFORM_HOST = "api.riotgames.com"

    _subdomains = [
        "br1", "eun1", "euw1", "jp1", "kr", "la1", "la2", "na1",
        "oc1", "tr1", "ru", "ph2", "sg2", "th2", "tw2", "vn2"
    ]

    _regions = ["americas", "asia", "europe", "sea"]

    PLATFORM_ROUTING_VALUES = None
    REGIONAL_ROUTING_VALUES = None

    @classmethod
    def initialize(cls):
        if cls.PLATFORM_ROUTING_VALUES is None:
            cls.PLATFORM_ROUTING_VALUES = {
                subdomain: f"{subdomain}.{cls.PLATFORM_HOST}" for subdomain in cls._subdomains
            }
        if cls.REGIONAL_ROUTING_VALUES is None:
            cls.REGIONAL_ROUTING_VALUES = {
                region: f"{region}.{cls.PLATFORM_HOST}" for region in cls._regions
            }

    @classmethod
    def extract_routing_value(cls, url: str):
        regex = r"(?:https?:\/\/)?(?:www\.)?([a-z0-9]+)\.api\.riotgames\.com"
        match = re.search(regex, url)
        return match.group(1) if match else None
