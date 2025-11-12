import confluent_kafka
import confluent_kafka.cimpl
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"confluent_kafka version: {confluent_kafka.__version__}")
    logger.info(f"cimpl module file: {confluent_kafka.cimpl.__file__}")
    logger.info(f"Current working directory: {os.getcwd()}")
    logger.info(f"sys.path: {os.sys.path}")

    return {"status": "ok"}
