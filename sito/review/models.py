from django.db import models

# Create your models here.
class candidates(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20,blank=True)
    email = models.EmailField(blank=True)
    programs = models.FileField(blank=True)
    about = models.SlugField(blank=True)
    dateTime = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return '{}'.format(self.firstName)
