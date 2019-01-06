import logging.config
import logging
import os
import yaml
import adafruit_bme680
import board
from busio import I2C


def setup_logging(path='logging.yml', default_level=logging.INFO, env_key='LOG_CFG'):
    """Setup logging configuration
    """
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def bme680_data():
    i2c = I2C(board.SCL, board.SDA)
    bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
    return {'temperature': bme680.temperature, 'gas': bme680.gas, 'humidity': bme680.humidity,
            'pressure': bme680.pressure, 'altitude': bme680.altitude}
        
