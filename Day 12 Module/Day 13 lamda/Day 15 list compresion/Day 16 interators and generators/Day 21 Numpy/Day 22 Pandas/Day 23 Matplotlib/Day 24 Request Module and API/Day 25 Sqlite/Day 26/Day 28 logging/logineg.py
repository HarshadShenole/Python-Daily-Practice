import logging 
logging.basicConfig(level=logging.DEBUG)
age = 20
logging.info("checking age")
if age >= 18:
    logging.info("Eligible")
else:
    logging.warning("Not Eligible")