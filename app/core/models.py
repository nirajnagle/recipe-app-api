from django.db import models
# Required to extend django User model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


#This is our User manager class. It is a class for creating user or super user 
class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves new user"""
        if not email:
            raise ValueError('Users must have email address')
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        
        return user
    
    def create_superuser(self, email,password):
        """Creates and saves a new super user"""
        user = self.create_user(email
                                ,password)
        user.is_staff= True
        user.is_superuser = True
        user.save(using=self.db)
        
        return user
        
# Create a Model class
#super user is included as part of permissions mixin        
class User(AbstractBaseUser,PermissionsMixin):
     """ Create user model that supports using email instead of username"""
     email = models.EmailField(max_length=255,unique=True)
     name = models.CharField(max_length=255)
     is_active = models.BooleanField(default=True)
     is_staff = models.BooleanField(default=False)
     
     objects= UserManager()
     
     USERNAME_FIELD = 'email'                                                 

