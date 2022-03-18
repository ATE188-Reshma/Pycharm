import logging

def errorlog(errormsg):
    logging.basicConfig(filename="../Automation/rr.log", format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt="%d/%m/%Y %H:%M:%S %p", level=logging.ERROR)
    aa = logging.getLogger()
    kk=aa.error(errormsg)
    return kk

def log1(info):

    logging.basicConfig(filename="../Automation/ss.log", format='%(asctime)s:%(levelname)s:%(message)s',
                        datefmt="%m/%d/%Y %H:%M:%S %p", level=logging.INFO)
    bb = logging.getLogger()
    cc = bb.info(info)
    return cc



