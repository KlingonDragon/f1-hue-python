import logging

from requests import post
from .type_def.f1_viewer import FlagColour, StatusFlagMap, StatusDataJSON

log = logging.getLogger(__name__)

STATUS_FLAG_MAP: StatusFlagMap = {"1": "GREEN", "2": "YELLOW", "3": "RED", "4": "SC"}


class F1ViewerConnection:
    def __init__(self, server: str, port: int):
        log.debug(f"Creating connection to {server} on port {port}")
        self.conn_url = f"http://{server}:{port}/api/graphql"

    def flag(self) -> FlagColour:
        log.debug("Getting flag colour")
        status: StatusDataJSON = post(
            self.conn_url, json={"query": "query StatusQuery {liveTimingState {TrackStatus}}"}
        ).json()
        log.debug(status)
        colour = STATUS_FLAG_MAP.get(
            status["data"]["liveTimingState"]["TrackStatus"]["Status"],
            "UNKNOWN",
        )
        log.info(f"Flag is {colour}")
        return colour
