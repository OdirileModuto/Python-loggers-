import logging.config
import json
import pathlib
import atexit
import os
import logging



if not os.path.exists('logs'):
    os.makedirs('logs')
  


logger = logging.getLogger("my_app")

def setup_logging():


    # specifies the path to the logging configuration file

    config_file = pathlib.Path("logging_configs/config.json")

    # opens the file, reads it, and loads the JSON content into the config variable

    with open(config_file, 'r') as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config)
  
    if queue_handler is not None and hasattr(queue_handler, 'listener'):
        queue_handler = next((h for h in logger.handlers if h.name == "queue_handler"))
  
    atexit.register(lambda: queue_handler.listener.stop())
   



def main():
    setup_logging()
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception('exception message')

         
# main(): runs the main function when the script is executed directly

if __name__ == '__main__':
    main()


