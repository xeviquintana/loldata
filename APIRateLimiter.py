import time
from collections import defaultdict

from RoutingValues import RoutingValues


class APIRateLimiter:
    """
    APIRateLimiter: manage developer key rate limits efficiently.

    limits - dict[str, tuple[int, int]]: i.e. 'euw1': (100, 120) 100 requests every 120 seconds
    """

    def __init__(self, limits):
        self.limits: dict[str, tuple[int, int]] = limits
        self.requests: defaultdict[str, list[float]] = defaultdict(list)

    @classmethod
    def with_default_limits(cls):
        RoutingValues.initialize()
        default_rate_limit = (100, 120)  # 100 requests every 120 seconds

        all_limits = {
            **{key: default_rate_limit for key in RoutingValues.PLATFORM_ROUTING_VALUES.keys()},
            **{key: default_rate_limit for key in RoutingValues.REGIONAL_ROUTING_VALUES.keys()},
        }

        return cls(limits=all_limits)

    def allow_request(self, routing_value: str):
        if routing_value not in self.limits:
            raise ValueError(f"No rate limit configured for routing value: {routing_value}")

        max_requests, time_window = self.limits[routing_value]
        current_time = time.time()

        # Remove requests older than the time window
        self.requests[routing_value] = [req for req in self.requests[routing_value] if current_time - req < time_window]

        if len(self.requests[routing_value]) < max_requests:
            self.requests[routing_value].append(current_time)
            return True

        return False
