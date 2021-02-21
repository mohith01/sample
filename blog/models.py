from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Posts(models.Model):
    Title = models.CharField(max_length=100)
    Date = models.DateField()
    Description = RichTextField(blank=False,null=True,max_length=500)
    Post = RichTextField(blank=False,null=True)
    #Post = models.TextField()

    def __str__(self):
        return self.Title

class Project(models.Model):
    Title = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='gallery/')
    Date = models.DateField()
    Shortdesc = RichTextField(blank=False)
    Description = RichTextField(blank=False,null=True)

    def __str__(self):
        return self.Title