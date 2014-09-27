from django.core.urlresolvers import reverse
from django.db import models

class Lecture(models.Model):
    TERM_CHOICES = (
        (u'S', u'summer'),
        (u'W', u'winter'),
        (u'A', u'allyear'),
    )
    
    lecture_id = models.IntegerField(primary_key=True)
    lecture = models.CharField(max_length=20)
    term = models.CharField(max_length=2, choices=TERM_CHOICES)

    def get_absolute_url(self):
        return reverse('lecture:detail', kwargs={'pk': self.pk})
        
    def __unicode__(self):
        return self.lecture
        

