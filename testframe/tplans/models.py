from django.db import models

class TestPlans(models.Model):
  DESIGN_PHASES = (
      ('ACPT', 'Acceptance'),
      ('BBFV', 'Building Block Functional Verification'),
      ('SDV', 'System Design Verification'),
      ('SIT', 'System Integration Test'),
      ('REGRESS', 'POST-GA Regression'),
  )

  name = models.CharField(max_length=128)
  created_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
  description = models.TextField(blank=True)
  phase = models.CharField(max_length=32, choices=DESIGN_PHASES, default='Acceptance')
  revision = models.PositiveSmallIntegerField(default=1)
  archived = models.BooleanField(default=False)

  def __str__(self):
    return "%s" % self.name
  def __unicode__(self):
    return u'%s' % self.name