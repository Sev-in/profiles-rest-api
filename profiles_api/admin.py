from django.contrib import admin #It includes Django's admin site-related tools and functions into your project.

from profiles_api import models 

admin.site.register(models.UserProfile) #Get the UserProfile model and display it on my admin site

# Register your models here.
