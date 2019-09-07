from django.db import models

# Create your models here.
class candidates(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField()
    about = models.SlugField()
    program = models.FileField(upload_to='programs/%Y/%m/%d/'+'CppTests.cpp')
    dateTime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{}'.format(self.firstName)
