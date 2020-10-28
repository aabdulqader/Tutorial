from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Tutorial




class TutorialAdmin(admin.ModelAdmin):


    # fields = [
    #     'title',
    #     'content'
    # ]


    fieldsets = [
        ('Title', {'fields':['title']}),
        ('Content', {'fields':['content']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }







admin.site.register(Tutorial, TutorialAdmin)
