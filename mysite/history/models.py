from django.core.urlresolvers import reverse
from django.db import models
import datetime

from lecture.models import Lecture
from django.contrib.auth.models import User

# Create your models here.

class History(models.Model):
    GRADE_CHOICES = (
        (u'S', u'S'),
        (u'A', u'A'),
        (u'B', u'B'),
        (u'C', u'C'),
        (u'D', u'D'),
    )

    YEAR_CHOICES = []
    for r in range(2010, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    year = models.IntegerField(max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)

    lecture = models.ForeignKey(Lecture)
    student = models.ForeignKey(User)

    class Meta:
        ordering = ["-year"]

    def get_absolute_url(self):
        return reverse('history:detail', kwargs={'pk': self.pk})
        
    def __unicode__(self):
        return u'%s %s %s %s' % (self.student, self.lecture, self.year, self.grade)
