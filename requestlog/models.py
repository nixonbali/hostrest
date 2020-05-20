from django.db import models

class RequestLog(models.Model):
    """Requests Table"""
    type = models.CharField(default="GET", max_length=16)
    time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(default=None, null=True)

    class Meta:
        db_table = 'requests'
        ordering = ['time']
