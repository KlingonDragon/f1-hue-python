import logging
from . import ARGS
from .f1_viewer import F1ViewerConnection

log = logging.getLogger(__name__)


def start():
    """Start the tool"""
    log.debug("start")
    print(F1ViewerConnection(ARGS.server, ARGS.port).flag())


if __name__ == "__main__":
    start()
