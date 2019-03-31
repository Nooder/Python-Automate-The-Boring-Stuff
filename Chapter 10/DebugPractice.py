#! python3
# Chapter 10 Project - Practice with debugging and logging

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

i = 10
#assert i == 9, "i does not equal 9"

logging.debug("This is a debug level log")
logging.info("This is an info level log")
logging.warning("This is a warning level log")
logging.error("This is an error level log")
logging.critical("This is a critical level log")

try:
    raise Exception("This is a raised exception")
except Exception:
    print("Caught the raised exception")

print("Done.")