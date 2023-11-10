from django.db import models

# Create your models here.
# Raw code for copy paste

class Classmate(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=300)
    gender = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('classmate_edit', kwargs={'pk': self.pk})

