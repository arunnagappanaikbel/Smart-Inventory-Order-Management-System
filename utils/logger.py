import logging
def setup_logger(log_file):
    logger = logging.getLogger("inventory_logger")
    logger.setLevel(logging.INFO)
    
    fh = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(fh)

    return logger
    
    