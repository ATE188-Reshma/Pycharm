import logging

def log1():
    # Name of the File to be created. Format->asctime to convert the tym which is understandable(s for string), level->log level, message->which is passed in Info
    logging.basicConfig(filename="../Automation/kk.log", format='%(asctime)s:%(levelname)s:%(message)s',
                        datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO)
    k = logging.getLogger()

# log1()
    return k

jj = log1()
jj.info("Reshma")
