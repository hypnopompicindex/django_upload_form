from django.db import models

class Upload(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/upload_form/get/%i/" % self.id