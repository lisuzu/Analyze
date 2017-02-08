 #-*-encoding=utf-8 -*-

from __future__ import unicode_literals

from django.db import models
import pymongo
conn = pymongo.MongoClient('localhost',27017)

class ErrorReManager(models.Manager):
    def inster(self,error,sultion,comment):
        db = conn['ErrorRe']
        mx = db.ErrorRe.find_one({'error': error})
        if mx is None:
            ID = db.ErrorRe.insert({'error':error,'sultion':sultion,'comment':comment})
            return ID
        else:
            return mx['_id']
    def custom_create(self,fileId,error,sultion,comment):
        ErrorRe_id = self.inster(error,sultion,comment)
        obj = self.create(fileId_id = fileId, ErrorRes=ErrorRe_id)
        return obj


# Create your models here.
class FileList(models.Model):
    name = models.CharField(max_length=255,verbose_name='名字')
    path = models.CharField(max_length=255,verbose_name='文件路径')
    tat = models.CharField(max_length=255,verbose_name='所属域')
    class Meta:
        app_label="upgrade"
        verbose_name = "文件列表"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class ErrorRe(models.Model):
    fileId = models.ForeignKey(FileList, max_length=255,verbose_name='文件列表')
    ErrorRes = models.CharField(max_length=255,verbose_name='正则表达式')
    objects = ErrorReManager()

    class Meta:
        app_label="upgrade"
        verbose_name = "正则存储表"
        verbose_name_plural = verbose_name
        ordering = ['-ErrorRes']

    def __unicode__(self):
        return self.ErrorRes


class Comment(models.Model):
    ErrorRe = models.ForeignKey(ErrorRe, max_length=255,verbose_name='正则表达试')
    comment = models.TextField(verbose_name='评论')
    grade = models.IntegerField(default=0,verbose_name='评分')
    create = models.DateTimeField(auto_now_add=True, verbose_name=u'更新时间')
    create_man = models.GenericIPAddressField(auto_created=True,verbose_name="创建人")
    class Meta:
        app_label="upgrade"
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        ordering = ['comment']
    def __unicode__(self):
        return self.comment

class ErrorSelfFile(models.Model):
    fileId = models.ForeignKey(FileList, max_length=255,verbose_name='__')
    ErrorSelfFile = models.ImageField()

