#!/usr/bin/env python3

import time
import logging
import os
import yaml
import helper
from pms5003py import pms5003


def main():

    # setup logger
    helper.setup_logging()
    logger = logging.getLogger(__name__)

    while True:
        sensor = pms5003()
        try:
            bme680 = helper.bme680_data()
            sensor.read_frame()
            print({**bme680, **sensor.data})
        except KeyboardInterrupt:
            print("\nTerminating data collection")
            break
        except:
            logger.debug("error", exc_info=True)
            break

if __name__ == '__main__':
    main()
