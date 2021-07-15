# from typing_extensions import Required
# from typing_extensions import Required
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, EmailField, IntegerField, TextField
from django.urls import	reverse
from django.utils import timezone






# Create your models here.
class Doctor(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    profile = models.ImageField(default="user.png", null=True, blank=True, upload_to="images")
    email = models.CharField(max_length=50)
    zip = IntegerField()
    address = CharField(max_length=250)
    city = CharField(max_length=50, null=True)
    state = CharField(max_length=50, null=True)

    def __str__(self):
        return self.firstname
    
class Patient(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    profile = models.ImageField(default="user.png", null=True, blank=True, upload_to="images")
    email = models.CharField(max_length=50)
    zip = IntegerField()
    address = CharField(max_length=250)
    city = CharField(max_length=50, null=True)
    state = CharField(max_length=50, null=True)

    def __str__(self):
        return self.firstname
    






class Post(models.Model):
    STATUS = (
    (0,"Draft"),
    (1,"Publish")
    )

    CATEGORY = (
        ("Mental Health","Mental Health"),
        ("Heart Disease","Heart Disease"),
        ("Covid19","Covid19"),
        ("Immunization","Immunization")

    )

    category = models.CharField(choices=CATEGORY, default='Mental Health', max_length=20)
    title = models.CharField(max_length=100, unique=True)
    pic = models.ImageField(default="blog.png", null=True, blank=True, upload_to="images")
    summery = models.CharField(max_length=200, unique=True)
    publish = models.DateTimeField(default=timezone.now)

    
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(Doctor, on_delete= models.CASCADE,related_name='blog_posts')

    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default='Draft')
    


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('account:post_detail',
                        args=[self.publish.year,
                              self.publish.month,
                              self.publish.day,
                              self.slug]                
                        )


    

    
