#!/usr/bin/python
#encoding:utf-8
import sys
import os
from .modelbase import ModelBase
#from modelbase import ModelBase

class JobOriginModel:
    
    def __init__(self):

        self.db = ModelBase('shixi')
        self.table = 'job_origin'

    def getJobInfoForWebPage(self, city = "", job_direction = "", publish_time = ""):
        if city == "" or job_direction == "" or publish_time == "":
            return {}
        sql = "select *, IF(month_salary != \'\', month_salary, day_salary) as salary, left(publish_time,10) as publish_date from %s where publish_time >= \'%s\' and city = \'%s\' and job_direction = \'%s\' order by publish_time desc" % (self.table, publish_time, city, job_direction)
        jobinfos = self.db.query(sql)
        return jobinfos

    def getJobInfoByTime(self, st = "", et = ""):
        if st == "" or et == "":
            return {}
        sql = "select * from %s where publish_time >= \'%s\' and publish_time < \'%s\'" % (self.table, st, et)
        jobinfos = self.db.query(sql)
        return jobinfos
    
    def insertone(self, item):
        def format(s):
            return str(s).replace('%', '%%')
        sql = "insert into %s(%s) values ('%s');" % (self.table, ",".join(item.keys()), "','".join(map(format, item.values())))
        #print sql
        ret = self.db.query(sql)
        if not ret:
            print sql
        
        
if __name__ == '__main__':
    #JobModel().getJobInfo()
    #JobModel().getJobInfo(city = "北京")
    #JobModel().getJobInfo( job_direction = "1")
    JobModel().getJobInfoForWebPage(city = "北京", job_direction = "1")
