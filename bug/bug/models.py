from django.db import models

class Bug(models.Model):
    BUG_TYPES = (
        ('error', 'error'),
        ('new feature', 'new feature'),
        ('enhancement', 'enhancement'),
        ('other', 'other')
    )

    STATUS = (
        ('To do','To do'),
        ('In Progress','In Progress'),
        ('Done','Done')
    ) 
    bug_description = models.TextField()
    report_date = models.DateField()
    bug_type = models.CharField(max_length=20, choices=BUG_TYPES)
    status = models.CharField(max_length=20, choices=STATUS)