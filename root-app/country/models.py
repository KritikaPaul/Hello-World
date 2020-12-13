from django.db import models

# Create your models here.


class country(models.Model):

    def __str__(self):
        return self.country_name


    country_name = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    country_image = models.ImageField(default='default.jpg',upload_to='country_image/')
    created_at = models.DateTimeField(auto_now_add=True)