from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class UserProfile(AbstractBaseUser, PermissionsMixin): #Inherits
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email' #This line tells Django which field to use for authentication (login).
    REQUIRED_FIELDS = ['name'] #So with this setting you are saying: "When creating an admin, it is not enough to ask for email and password, you must also ask for the name field."

    def get_full_name(self):
        """Retrive full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrive short name of user"""
        return self.name
    
    def __str__(self):
        """Return string representation of our user"""
        return self.email

