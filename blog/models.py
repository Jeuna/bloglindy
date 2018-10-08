from __future__ import unicode_literals

from django.db import models


from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
# Create your models here.
from django.contrib.auth.models import User

class Blog(models.Model):

    title = models.CharField(max_length=255, null=False, blank=False,)
    content = RichTextUploadingField(null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    background_image = models.ImageField(upload_to='blogresimleri/%Y/%m/%d', default='blogresimleri/mexico.jpg')
    slug = models.SlugField(max_length=80, null=True, help_text=u"Automatic link, pelase dont change!")  # slug
    link = models.URLField(blank=True,null=True)
    about = models.TextField(blank=True,null=True)

    def __unicode(self):
        return '{}'.format(self.title)


