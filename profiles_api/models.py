from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have a email address')
        email =  self.normalize_email(email) # @GMAIL.com -> @gmail.com
        user = self.model(email=email, name=name)

        user.set_password(password) # For security
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,name,password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



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
    

class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey( #It creates a connection 🔗 between a post and the user who shared it.
        settings.AUTH_USER_MODEL, #Instead of writing models.UserProfile directly, it tells Django to "Use whatever is defined as the user model in your project's settings (settings.py). This makes your code more flexible and reusable.
        on_delete= models.CASCADE #If the user who owns this post is deleted from the database, all posts by that user will be automatically deleted as well.
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text

