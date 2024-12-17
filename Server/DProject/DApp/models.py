from django.db import models

# Create your models here.
class Member(models.Model):
    memberName = models.CharField(max_length=20)
    memberNIK = models.CharField(max_length=20)

    def __str__(self):
        return self.memberNIK