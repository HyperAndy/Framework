import sys
import logging
from src.utils.config import Config
from src.utils.logger import setup_logger

def main():
    cfg = Config.fromfile('../src/config/testa.py')
    print(cfg)

    # init logger before other steps
    logger = setup_logger(logging.DEBUG)
    logger.info('test: {}'.format('pass'))


if __name__ == '__main__':
    main()



