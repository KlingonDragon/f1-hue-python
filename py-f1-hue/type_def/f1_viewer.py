from typing import Literal, TypedDict

StatusCode = Literal["1", "2", "4", "5", "6"]
FlagColour = Literal["GREEN", "YELLOW", "SC", "RED", "VSC", "UNKNOWN"]
StatusFlagMap = dict[StatusCode, FlagColour]


class _TrackStatus(TypedDict):
    Status: StatusCode
    Message: str


class _LiveTimingState(TypedDict):
    TrackStatus: _TrackStatus


class _StatusData(TypedDict):
    liveTimingState: _LiveTimingState


class StatusDataJSON(TypedDict):
    data: _StatusData
