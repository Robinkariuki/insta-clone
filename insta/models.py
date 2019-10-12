from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    
    p_pic = models.ForeignKey(User, related_name='profile_pic', blank=True, default=1)
    post = models.ImageField(upload_to = 'posts/', blank=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    image_name = models.CharField(max_length = 30, default='my-image')
    caption = models.CharField(max_length = 200)
    location = models.CharField(max_length=30)
    likes = models.IntegerField()
    post_date = models.DateTimeField(auto_now_add=True)


    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
 


    def __str__(self):
        return self.image_name
