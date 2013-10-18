from django.db import models
from django.contrib.auth.models import User

DISABLE_CHOICES = ((1,'Enable'),(0,'Disable'))

class ContactUs(models.Model):
#    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 80, verbose_name ='Name')
    address = models.TextField(null = True, verbose_name ='Address', max_length = 400)
    status = models.IntegerField( default = 1, choices = DISABLE_CHOICES, verbose_name ='Status')
    phone_no = models.IntegerField(max_length = 22,  verbose_name ='Phone No')
    email_id = models.EmailField()
    creation_date = models.DateTimeField(auto_now_add=True)
    moderation_date = models.DateTimeField(auto_now=True)
    done_by = models.ForeignKey(User,null=True)

    def __unicode__(self):
        if self.name:
            return '%s' % (self.name)



# Create your models here.
