from django.contrib import admin
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







admin.site.register(Tutorial, TutorialAdmin)
