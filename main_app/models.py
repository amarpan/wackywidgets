from django.db import models
from django.urls import reverse

class Widget(models.Model):
    description = models.CharField(max_length=50)
    quantity = models.IntegerField() #good with empty parantheses here

    def __str__(self):
        return self.description
    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'cat_id': self.id})
    def get_absolute_url(self):
        return reverse('index', kwargs={'widget_id': self.id})