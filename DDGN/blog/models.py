from django.db import models
from django.utils.text import slugify
# Create your models here.

from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    # Class Category to organize posts according to
    title = models.CharField(max_length=255, verbose_name='title')
    slug = models.SlugField(default='', blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def save(self, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save()

    def __str__(self):
        return self.title


class Post(models.Model):
    # Class post
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True, config_name='description')
    text = RichTextUploadingField(blank=True, null=True, config_name='special',
                                  external_plugin_resources=[(
                                      'youtube',
                                      '/static/base/vendor/ckeditor_plugins/youtube/youtube/',
                                      'plugin.js',
                                  )],
                                  )
    category = models.ForeignKey(Category, verbose_name="Category", blank=True, null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(default='', blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def save(self, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return self.title
