from django.db import models
from django.contrib import admin

class TitleDeedAdmin(admin.ModelAdmin):

    List_Filter = ('Title_Number',)

class TitleDeed (models.Model):

    Title_Number = models.CharField(max_length = 200)

    Full_Names = models.CharField(max_length = 200)

    Title_Image = models.ImageField(upload_to='images/', default="images")

    def __str__(self):
       return self.Title_Number
