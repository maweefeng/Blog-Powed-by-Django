from django.contrib import admin

# Register your models here.

from .models import Article,Summary

admin.site.register(Article)
admin.site.register(Summary)