from django.contrib import admin
from app007 import models
from ..common.decorator import singleton
#from django.db import models
# Register your models here.

@singleton
class JobTable():

    def __init__(self):

        self.table =  'job'
        print 'diaoyong888888888888888888888 '

    def listProjects(self):
        return [(item.project,item.create_time,item.password) for item in self.o_project.all()]

    def newProject(self, new_project, new_password):
        dic = {'project' : new_project, 'password' : new_password}
        ret = self.o_project.create(**dic)
        return ret

    def delProject(self, project_name):
        ret = self.o_project.filter(project = project_name).delete()
        return ret

    def getProjectByProjectPassword(self, project_name, password):
        ret = self.o_project.get(project = project_name, password = password)
        return ret



