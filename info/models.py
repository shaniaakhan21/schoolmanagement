from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField(null = True , blank = True)
    img = models.ImageField(null = True, blank = True)
    qualification = models.CharField(max_length=200)
    salary = models.FloatField()
    age = models.IntegerField()
    phonenumber = models.IntegerField() #without country code
    aadaharid = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)
	#slug = models.SlugField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try :
            url = self.img.url
        except:
        	url = ''
        return url


class Notice(models.Model):
    subject = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    published = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length = 100)
    textcontent = models.TextField(null = True, blank = True)
    Filename = models.CharField(max_length = 50,null = True, blank = True)
    Fileupload = models.FileField(null = True, blank = True  )


    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title

"""
class Post(models.Model):
    posttitle = models.CharField(max_length = 100)
    postpublished = models.DateTimeField(default=timezone.now)
    postauthor = models.ForeignKey(User, on_delete=models.CASCADE)
    postcontent = models.TextField(null = True, blank = True)
    postcontentimg = models.ImageField(null = True, blank = True)
    postcontentfile = models.FileField(null = True, blank = True)
"""
class Assignment(models.Model):
    subject = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    standard =models.CharField(max_length= 20 , null = True , blank = True)
    section = models.CharField(max_length = 10, null = True , blank = True)
    branch = models.CharField(max_length = 10 , null = True , blank = True )
    published = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length = 100)
    textcontent = models.TextField(null = True, blank = True)
    Filename = models.CharField(max_length = 50,null = True, blank = True)
    Fileupload = models.FileField(null = True, blank = True  )

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title
