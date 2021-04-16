# ! /usr/bin/env python3


__package_name__ = 'rpi_temp_humid_logger'
__version__ = '0.1.0dev1'
__author__ = 'Aaron kHz Greenyer'
__author_email__ = 'akgreenyer@gmail.com'
__description__ = 'Raspberry Pi logger for measuring humidity and temperature with the DHT22'
__url__ = 'https://github.com/akgre/rpi_temp_humid_logger'
__license__ = 'MIT WITHOUT ANY WARRANTY'
__copyright__ = 'Copyright (C) 2020 Aaron kHz Greenyer'

from argparse import ArgumentParser
from utils.easy_logging import setup_logging
from loguru import logger


class RPITempHumidLogger(object):
    """@brief Responsible for measuring humidity and temperature with the DHT22."""

    def __init__(self):
        """@brief Constructor"""
        pass

    def execute(self):
        """@brief Execute the logging."""
        pass


# Main.
# ------------------------------------------------------------------------------
def _main():

    parser = ArgumentParser(description=f"{__package_name__} Version {__version__}\n{__description__}")
    parser.add_argument("--version",
                        action="version", version=__version__,
                        help="Display version information and dependencies."
                        )
    parser.add_argument("--verbose", "-v", "-d", "--debug",
                        action="store_true", dest="verbose", default=False,
                        help="Display extra debugging information and metrics."
                        )
    parser.add_argument("--user", "-u",
                        action="store_true", dest="user", default=True,
                        help="Show the options selection GUIcl"
                        )

    args = parser.parse_args()

    try:
        # if logging gui is cancelled then exit
        if not setup_logging(user_input=args.user, project_name=__package_name__):
            exit()
        app = RPITempHumidLogger()
        app.execute()
    except KeyboardInterrupt:
        logger.warning('Keyboard Interrupt from user')
    except Exception as ex:
        if args.verbose:
            logger.exception(ex)
        else:
            logger.error(f'Fatal error!\n\nTest sequence generator crashed.\n\nReason: {str(ex)}')


if __name__ == "__main__":
    _main()

