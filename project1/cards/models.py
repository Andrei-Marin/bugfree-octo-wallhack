from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Cards(models.Model):

    owner = models.ForeignKey(User)
    url_name = models.URLField()
    card_name = models.CharField(max_length=60)
    image = models.ImageField(default='')
    media_type = models.CharField(max_length=32)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.card_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

