#!/usr/bin/env python
#encoding:utf-8
from peewee import (Model, IntegerField, CharField, DateTimeField, TextField, PrimaryKeyField, ForeignKeyField, DateField, FloatField, BigIntegerField)
from peewee import MySQLDatabase

def _utf_string(s):
    if isinstance(s, unicode):
        return s.encode("utf-8", "ignore")
    return str(s)

#model的基础类
class ModelBase(object):

    def __init__(self, dbname):
        
        self.dbname = dbname
        self.oDbBase = ''
        self.__connect()


    def __connect(self):

        if self.dbname == 'shixi':
            self.oDbBase = MySQLDatabase('shixi', **{'host': '127.0.0.01', 'password': 'uAiqwVwjJ8-i', 'port': 3306, 'user': 'root', 'charset': 'utf8'})
        if self.dbname == 'coopin':
            self.oDbBase = MySQLDatabase('coopinion', **{'host': '192.168.241.32', 'password': 'OOpin2007Group', 'port': 3306, 'user': 'oopin', 'charset': 'utf8'})




    def query(self, sql):
        '''
            input :  sql
            output : data from table

        '''
        if not self.oDbBase:
            self.__connect()

        data_list = []
        result = self.oDbBase.execute_sql(sql)
        for array in result:
            data_map = {}
            j = 0
            for value in array:
                if type(value) == unicode:
                    value = value.encode('utf-8')
                data_map[result.description[j][0].encode('utf-8')] = value
                j += 1
            data_list.append(data_map)
        return data_list

    def operate(self, sSql):

        '''
            input : sSql
            ret : bool True->success False->failure

        '''

        if not self.oDbBase:
            self.__connect()

        bRet = self.oDbBase.execute_sql(sSql)

        return bRet

    def close(self):
        self.oDbBase.close()
        
#print ModelBase().operate("insert into brands(brands_name, positive_limit, reverse_limit, is_noise, remain2, remain1) values('b','a','a','a','a',1)")
#print ModelBase().operate("update brands set brands_name='c' where brands_name='b'")
