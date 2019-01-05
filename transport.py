#encoding:utf-8
import datetime
from datetime import timedelta
from model.t_job import JobModel as JobM
from model.t_job_origin import JobOriginModel as JoboM 
from checksum import checksum
from label import label
import sys
import esm

def loadbigFactory():
    index = esm.Index()
    with open('bigfactory', 'r') as fr:
        for line in fr:
            line = line.strip()
            if line == "":
                continue
            index.enter(line)
    index.fix()
    return index


if __name__ == "__main__":
    si = -1 
    se = 0
    sd = (datetime.date.today() + timedelta(days = si)).strftime("%Y-%m-%d")  
    ed = (datetime.date.today() + timedelta(days = se)).strftime("%Y-%m-%d")  

    print 'begin to transport [%s, %s) ......' % (sd, ed)
    jobinfos=JoboM().getJobInfoByTime(sd, ed)
    if len(jobinfos) == 0:
        print "no data in [%s, %s)" % (sd, ed)
        sys.exit()
 
    print 'total: %s' % (len(jobinfos))
    jobm = JobM()
    index = loadbigFactory()
    for item in jobinfos:
        item.pop("id")

        #checksum
        ret, item = checksum(item)
        if not ret:
            continue

        #label
        label(index, item)

        #other
        jobm.insertone(item)
       # sys.exit()
 
        
