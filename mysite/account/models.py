from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    GRADE_CHOICES = (
        (u'U1', u'U1'),
        (u'U2', u'U2'),
        (u'U3', u'U3'),
        (u'U4', u'U4'),
    )
    todai_id = models.CharField(max_length=20)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    
    def __unicode__(self):
        return self.user.username


