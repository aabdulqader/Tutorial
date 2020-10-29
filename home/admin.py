from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Tutorial, TutorialSeries, TutorialCategory




class TutorialAdmin(admin.ModelAdmin):


    # fields = [
    #     'title',
    #     'content'
    # ]


    fieldsets = [
        ('Title', {'fields':['title']}),
        ("URL", {'fields': ["tutorial_slug"]}),
        ("Series", {'fields': ["tutorial_series"]}),
        ('Content', {'fields':['content']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }







admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
