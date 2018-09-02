"""A package to log broadband speed test results"""
import datetime
import logging
import sys

import click
import daiquiri
from speedtest import ConfigRetrievalError, Speedtest, SpeedtestConfigError

__version__ = "0.0.8"


@click.command()
@click.argument("directory", type=click.Path(), default=".")
def main(directory):
    daiquiri.setup(
        level=logging.INFO,
        outputs=[
            daiquiri.output.TimedRotatingFile(
                filename="speedtest.log",
                directory=directory,
                level=logging.INFO,
                interval=datetime.timedelta(weeks=1),
                formatter=daiquiri.formatter.ColorFormatter(fmt="%(message)s"),
            )
        ],
    )
    logger = daiquiri.getLogger(__name__)
    servers = []

    try:
        s = Speedtest()
        s.get_servers(servers)
        s.get_best_server()
        s.download()
        s.upload(pre_allocate=False)
        message = s.results.csv()
    except (ConfigRetrievalError, SpeedtestConfigError):
        message = f",,,{datetime.datetime.utcnow().isoformat()}Z,,,0,0,,"

    logger.info(message)
