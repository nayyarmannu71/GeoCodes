from django.db import models


# Create your models here.
class GeoFiles(models.Model):
    document = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)