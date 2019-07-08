from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 


class Profile(models.Model):
    user_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Category(models.Model):
    name = models.CharField(max_length=120,blank=False)
    


def user_directory_path(category, filename):
    return '{0}/{1}'.format(category, filename)

class Book(models.Model):
    title = models.CharField(max_length=120,blank=False)
    description = models.TextField()
    uploaded_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, blank=True)
    image = models.ImageField(upload_to='coverImage/', blank=True)
    upload = models.FileField(upload_to=user_directory_path) 

    @classmethod
    def get_all_books_in_a_category(cls, category):
        books = cls.object.filter(category__category=categorys_name)