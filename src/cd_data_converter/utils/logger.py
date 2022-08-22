import logging

logging.basicConfig(format="[%(levelname)s] %(asctime)s | %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
