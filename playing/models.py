from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
# Create your models here.
class Play(models.Model):
    name=models.CharField(max_length=255, null=False, blank=True)
    purchaser=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    desc=models.TextField()
    img=models.TextField(default= "no image provided")
    
 
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('play_list')  