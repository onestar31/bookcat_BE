from django.db import models

class User(models.Model):
    userName = models.CharField(max_length = 20)
    userEmail = models.EmailField(max_length = 30)
    userPw = models.CharField(max_length = 20)

    class Meta:
        db_table = 'users'