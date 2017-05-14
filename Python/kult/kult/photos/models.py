from django.db import models

# Create your models here.


class Photo(models.Model):
    upload = models.FileField(upload_to='uploads/%Y%m/%d')
    upload_date = models.DateTimeField(auto_now=True)
    width = models.PositiveSmallIntegerField(default=0)
    height = models.PositiveSmallIntegerField(default=0)
    format = models.CharField(max_length=20)
    # TODO: add exif information

    def __str__(self):
        return "%s, %s" % (str(self.upload), str(self.upload_date))


class PhotoDescription(models.Model):
    SAFE_SEARCH = 'SS'
    LABELS = 'LA'
    WEB_DESC = 'WD'
    DESC_TYPE_CHOICES = (
        (SAFE_SEARCH, 'Safe search'),
        (LABELS, 'Labels'),
        (WEB_DESC, 'Web description')
    )
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    desc_type = models.CharField(max_length=2, choices=DESC_TYPE_CHOICES)
    description = models.CharField(max_length=50)
