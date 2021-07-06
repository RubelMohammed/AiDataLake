# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#Removed django & security related model information from the schema
class RequestTable(models.Model):
    requesttimestamp = models.DateTimeField(db_column='requestTimeStamp')  # Field name made lowercase.
    requesttext = models.TextField(db_column='requestText')  # Field name made lowercase.

    class Meta:
        db_table = 'requesttable'


class UserLogin(models.Model):
    username = models.TextField()
    password = models.TextField()
    dateaccountcreated = models.DateField(db_column='dateAccountCreated')  # Field name made lowercase.
    loginstatus = models.IntegerField(db_column='loginStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'userlogin'


class UserTable(models.Model):
    requesttext = models.TextField(db_column='requestText')  # Field name made lowercase.
    metageneration = models.TextField(db_column='metaGeneration')  # Field name made lowercase.
    sqloutput = models.TextField(db_column='sqlOutput')  # Field name made lowercase.
    id = models.IntegerField()
    requestdatetime = models.DateTimeField(db_column='requestDateTime')  # Field name made lowercase.

    class Meta:
        db_table = 'usertable'

	