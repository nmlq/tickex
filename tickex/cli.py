import os
import logging
from tickex import pipeline
from tickex import extractors
from tickex import translators
from tickex import loaders


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def validate_envvars(
        envvars: list = ["MONGO_PASS", "MONGO_URI", "MONGO_USER"]):
    for envvar in envvars:
        if envvar not in os.environ:
            raise ValueError("Not all environment variables available; {envvars}")

def main():
    logger.info("Starting CLI for tickex")
    validate_envvars()
    logger.info("Validated environment variables")

    logger.info("Starting the ETL pipeline")
    pipeline.Pipeline(
        extractor=extractors.YahooExtractor(),
        translator=translators.YahooTranslator(),
        loader=loaders.MongoLoader(
            user=os.environ['MONGO_USER'],
            password=os.environ['MONGO_PASS'],
            uri=os.environ['MONGO_URI']
        )
    ).run()
    logger.info("Completed running the ETL pipeline")


if __name__ == "__main__":
    logger.info(f"Running main; {__name__}")
    main()