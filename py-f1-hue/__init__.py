import argparse, logging


# Args init #
class _ArgNamespace(argparse.Namespace):
    log_level: int
    """Log level determined by args"""
    server: str
    """host server domain/ip"""
    port: int
    """port number"""


_arg_parser = argparse.ArgumentParser()
_arg_parser.add_argument(
    "--debug",
    help="Start tool in debug mode",
    action="store_const",
    dest="log_level",
    const=logging.DEBUG,
    default=logging.INFO,
)
_arg_parser.add_argument("--server", default="localhost")
_arg_parser.add_argument("--port", default=10101)

ARGS = _arg_parser.parse_args(namespace=_ArgNamespace())
"""Parsed args"""


# Logging init #
logging.basicConfig(
    filename=f"{__package__}.log",
    format="{asctime} [{levelname}] {name}:{funcName} L{lineno} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
    level=ARGS.log_level,
)
