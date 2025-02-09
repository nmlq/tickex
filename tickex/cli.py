import os
import logging
from tickex import pipeline
from tickex import extractors
from tickex import translators
from tickex import loaders


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def validate_envvars(
        envvars: list = [
            "MONGO_PASS",
            "MONGO_URI",
            "MONGO_USER",
            "MONGO_PROTOCOL"]) -> None:
    """Check for required environment variables.

    :return None:
    :raises ValueError: exception on missing environment variables
    """
    for envvar in envvars:
        if envvar not in os.environ:
            raise ValueError(f"Not all env vars available; {envvars}; Missing '{envvar}'")


def main() -> None:
    """Main cli call, run the ETL pipeline.

    :return None:
    """
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
            uri=os.environ['MONGO_URI'],
            protocol=os.environ['MONGO_PROTOCOL']
        )
    ).run()
    logger.info("Completed running the ETL pipeline")


if __name__ == "__main__":
    logger.info(f"Running main; {__name__}")
    main()
