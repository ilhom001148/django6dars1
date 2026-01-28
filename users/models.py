from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timezone, datetime, timedelta


class CustomUser(AbstractUser):
    address=models.CharField(max_length=50,null=True,blank=True)
    phone=models.CharField(max_length=13,null=True,blank=True)

    def __str__(self):
        return f'username:{self.username}'


class EmailCode(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='email_codes')
    code=models.CharField(max_length=6)
    created_at=models.DateTimeField(auto_now_add=True)
    is_activated=models.BooleanField(default=False)
    expires_at=models.DateTimeField(null=True,blank=False)

    def is_expired(self, *args,**kwargs):
        self.expires_at=datetime.now()+timedelta(minutes=2)
        super(EmailCode,self).save(*args,**kwargs)


#
# class EmailCode(models.Model):
#     user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
#     code = models.CharField(max_length=6)
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_activated = models.BooleanField(default=False)
#
#     def is_expired(self):
#         return timezone.now() > self.created_at + timedelta(minutes=2)


