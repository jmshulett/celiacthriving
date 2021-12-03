from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class ShopTips(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    tip_desc = models.TextField()
    slug = models.SlugField(max_length=200,
                            unique=True)
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='tips')
    class Meta:
        ordering = ('name',)
        verbose_name = 'tip'
        verbose_name_plural = 'tips'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tips:tips_detail',
                       args=[self.id, self.slug]) 
