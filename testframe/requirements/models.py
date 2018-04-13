from django.db import models

# Create your models here.
class Requirements(models.Model):
  name = models.CharField(max_length=128)
  created_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
  description = models.TextField(blank=True)
  revision = models.PositiveSmallIntegerField(default=1)
  archived = models.BooleanField(default=False)

  def __str__(self):
    return "%s" % self.name
  def __unicode__(self):
    return u'%s' % self.name