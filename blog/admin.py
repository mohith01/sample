from django.contrib import admin
from django.db import models
# Register your models here.
from .models import Posts,Project


admin.site.register(Posts)
admin.site.register(Project)