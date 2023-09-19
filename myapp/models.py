from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(unique=True)
    avatar = models.CharField(max_length=255)
    oauth_token = models.CharField(max_length=255)

    def __str__(self):
        return self.username  



class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=20 )
    description= models.CharField(max_length=100)
    owner_id= models.ForeignKey(User.user_id)
    created_at= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.group_name


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name= models.CharField(max_length=50)
    start_date= models.DateField(auto_now_add=True)
    end_date= models.DateField()
    locaion= models.CharField(max_length=100)
    description= models.CharField(max_length=100)

    def __str__(self):
        return self.event_name

class User_group(models.Model):
    user= models.ForeignKey("User")
    event= models.ForeignKey("Event")



class Event(models.Model):
    """Model representing an event."""
    id = models.AutoField(primary_key=True, max_length=60)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=1024)
    creator_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    location = models.CharField(max_length=1024)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    thumbnail=models.ImageField(blank=True,upload_to='events/') 

    class Meta:
        verbose_name ='Event'
        verbose_name_plural = ("Events")
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
      