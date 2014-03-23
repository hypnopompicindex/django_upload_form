from django.db import models


def get_upload_file_name(instance, filename):
    return settings.UPLOAD_FILE_PATTERN % (str(time()).replace('.','_'), filename)


class Upload(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    file = models.FileField(upload_to=get_upload_file_name)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/upload_form/get/%i/" % self.id