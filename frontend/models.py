# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#Removed django & security related model information from the schema

class UserLogin(models.Model):
    username = models.TextField()
    password = models.TextField()
    dateaccountcreated = models.DateField(db_column='dateAccountCreated')  # Field name made lowercase.
    loginstatus = models.IntegerField(db_column='loginStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'userlogin'


class GptInputOutput(models.Model):
    userInput = models.TextField(db_column='userInput')  # Field name made lowercase.
    fullRequestInput = models.TextField(db_column='fullRequestInput')  # Field name made lowercase.
    gptOutput = models.TextField(db_column='gptOutput')  # Field name made lowercase.
    sqlGeneration = models.BooleanField(db_column='sqlGeneration')
    requestDateTime = models.DateTimeField(db_column='requestDateTime')  # Field name made lowercase.

    class Meta:
        db_table = 'GptInputOutput'

class UserDatabase(models.Model):
    dbName = models.CharField(max_length=50)
    userId = models.ForeignKey("UserLogin", on_delete=models.CASCADE)
    schemaString = models.TextField(db_column='schemaString')

    class Meta:
        db_table = 'UserDatabase'

class UserDatabaseEntity(models.Model):
    databaseId = models.ForeignKey("UserDatabase", on_delete=models.CASCADE)
    userId = models.ForeignKey("UserLogin", on_delete=models.CASCADE)
    tableOrColumn = models.CharField(max_length=50)
    dataType = models.Charfield(max_length=50)
    localGroupingKey = models.IntegerField(db_column='localGroupingKey')
    description = models.CharField(max_length=50)

    class Meta:
        db_table = 'UserDatabaseEntity'
