def foo():
    return "bar"


if __name__ == "__main__":
    from argparse import ArgumentParser

    import colorlog

    parser = ArgumentParser(description="My app which is mine")

    parser.add_argument(
        "-ll",
        "--loglevel",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level",
    )

    args = parser.parse_args()

    colorlog.logging.basicConfig(level=args.loglevel)
    logger = colorlog.getLogger()

    logger.debug("This is for debugging. Very talkative!")
    logger.info("This is for normal chatter")
    logger.warning("Warnings should almost always be seen.")
    logger.error("You definitely want to see all errors!")
    logger.critical("Last message before a program crash!")
