from django.db import models

class TestCaseCategories(models.Model):
  category = models.CharField(max_length=64)

  def __str__(self):
    return "%s" % self.category
  def __unicode__(self):
    return u'%s' % self.category

class TestCases(models.Model):
  name = models.CharField(max_length=128)
  created_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
  description = models.TextField(blank=True)
  test_category = models.ForeignKey(TestCaseCategories, on_delete=models.CASCADE)
  revision = models.PositiveSmallIntegerField(default=1)
  archived = models.BooleanField(default=False)

  def __str__(self):
    return "%s" % self.name
  def __unicode__(self):
    return u'%s' % self.name