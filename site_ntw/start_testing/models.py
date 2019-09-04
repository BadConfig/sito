from django.db import models

# Create your models here.
class candidates_data(models.Model):
    first_name      = models.CharField(max_length=20)
    last_name       = models.CharField(max_length=20)
    email           = models.EmailField()
    telegram_contact= models.CharField(max_length=20)
    about_candidate = models.TextField()
    solved_quizez   = models.FileField(upload_to='quizez/%Y/%m/%d/')
    datetime_of_reqw= models.DateTimeField(auto_now_add=True)
    
        
