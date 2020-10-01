#!/usr/bin/env python3
import logging
from pathlib import Path

from hide_sidebars.main import main

LOG_FILE = Path(__file__).resolve().parent / "logs" / "dhs.log"
# Change this to `logging.WARN` and redact all personal information before sharing logs!
LOG_LEVEL = logging.DEBUG

if __name__ == "__main__":
    logging.basicConfig(
        filename=LOG_FILE,
        filemode="w",
        datefmt='%H:%M:%S',
        level=LOG_LEVEL
    )

    main()
