from django.db import models

class HQ(models.Model):
    
    name_hq = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publishing_company = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_hq
    