import os
from django.db import models

from pycon.sponsors.enums import SponsorLevels


class Sponsor(models.Model):

    def upload_path(self, filename):
        return os.path.basename(filename)

    description_en = models.TextField(max_length=512)
    description_fr = models.TextField(max_length=512)
    logo_en = models.ImageField(max_length=512, upload_to=upload_path)
    logo_fr = models.ImageField(max_length=512, upload_to=upload_path)
    name_en = models.CharField(max_length=128)
    name_fr = models.CharField(max_length=128)
    level = models.CharField(max_length=64, choices=SponsorLevels.choices)
    url_twitter_en = models.URLField(blank=True)
    url_twitter_fr = models.URLField(blank=True)
    url_website_en = models.URLField(blank=True)
    url_website_fr = models.URLField(blank=True)
