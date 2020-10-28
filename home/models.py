from django.db import models

class Tutorial(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title[:35] + ' | ' + self.content[:30]

    
    

