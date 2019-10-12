from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save


Gender=(
    ('Male','Male'),
    ('Female','Female'),
)
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

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profilepics/', default = 'profilepics/default.jpg')
    bio = HTMLField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    
    email= models.EmailField()
    gender = models.CharField(max_length=15,choices=Gender,default="Male")


    @classmethod
    def search_profile(cls,search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term)
        return profiles

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username