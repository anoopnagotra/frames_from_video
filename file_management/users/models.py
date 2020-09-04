from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import UserManager
from django.conf import settings

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import EmailMessage


USER_TYPE = (
        ('user', 'user'),
        ('toc', 'toc')
    )

STATES = (
        ('BW', 'Baden-Württemberg'),
        ('BY', 'Bayern'),
        ('BE', 'Berlin'),
        ('BB', 'Brandenburg'),
        ('HB', 'Bremen'),
        ('HH', 'Hamburg'),
        ('HE', 'Hessen'),
        ('MV', 'Mecklenburg-Vorpommern'),
        ('NI', 'Niedersachsen'),
        ('NW', 'Nordrhein-Westfalen'),
        ('RP', 'Rheinland-Pfalz'),
        ('SL', 'Saarland'),
        ('SN', 'Sachsen'),
        ('ST', 'Sachsen-Anhalt'),
        ('SH', 'Schleswig-Holstein'),
        ('TH', 'Thüringen')
    )

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.EmailField(_('username'), unique=False, blank=True,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    password = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    name = models.CharField(max_length=200,blank=False)
    mobile_number = models.CharField(max_length=20,blank=True)
    primary_number = models.CharField(max_length=20,blank=True)
    
    mobile_number_verified =  models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    account_activation_token = models.CharField(max_length=100,blank=True)
   
    address = models.TextField(max_length=200,blank=True)
    city = models.CharField(max_length=120,blank=True)

    state = models.CharField(choices=STATES, max_length=120,blank=True)
    
    country = models.CharField(max_length=120,blank=True)
    postal_code = models.CharField(max_length=20,blank=True)
    total_purchases = models.CharField(max_length=20,blank=True)
    forgot_password_token = models.CharField(max_length=100,blank=True)
    file_sharing_token = models.CharField(max_length=100,blank=True)
    
    status = models.BooleanField(default=False)
    role = models.CharField(choices=USER_TYPE, default='user', max_length=250, blank=False, unique=False)
    tax_number = models.CharField(max_length=250, blank=False)
    profile_image = models.CharField(max_length=250, blank=False)
    profile_image_path = models.CharField(max_length=250, blank=False)
    
    file_encryption_key = models.CharField(max_length=250, blank=True, null=True)
    users_under_toc = models.TextField(max_length=1500, blank=True, null=True)
    one_to_one_share_uid = models.TextField(max_length=1500, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at =models.DateTimeField(auto_now=True, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    # def save(self):
    #     if self.send_it:
    #         #First you create your list of users
    #         user_list = []
    #         for u in self.users:
    #             user_list.append(u.email)

    #         #Then you can send the message. 
    #         send_mail(str(self.subject), 
    #                   str(self.message),
    #                   'from@example.com',
    #                   user_list, 
    #                   fail_silently=False)


class MyVideo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    full_path = models.CharField(max_length=255, blank=True)
    status =  models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at =models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "MyVideos"
