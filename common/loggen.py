import logging,time,os
class Loggen(object):
    def __init__(self,logname):
        self.log=logging.getLogger(logname)
        self.log.setLevel(logging.INFO)
        tr=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        path=os.path.abspath(os.path.dirname('.'))+"//logs//"+tr+".log"
        file=logging.FileHandler(path)
        file.setLevel(logging.INFO)
        controltext=logging.StreamHandler()
        controltext.setLevel(logging.INFO)
        formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        file.setFormatter(formatter)
        controltext.setFormatter(formatter)
        self.log.addHandler(file)
        self.log.addHandler(controltext)
    def getlog(self):
        return self.log