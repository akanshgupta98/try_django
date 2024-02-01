from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):

    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte = now)
class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model,using=self._db)

    def published(self):
        return self.get_queryset().published()

# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,default=1)
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False,blank = True, null=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    # date = models.DateTimeField(blank=True, auto_now = True)
    slug = models.SlugField(default = "hello-world",unique=True)
    objects = BlogPostManager()

    class Meta:
        ordering = ['-publish_date','-updated','-timestamp']

    def get_retrieve_url(self):
        return f'/blogs/retrieve/{self.slug}'
    
    def get_edit_url(self):
        return f'/blogs/{self.slug}/edit'
    
    def get_delete_url(self):
        return f'/blogs/{self.slug}/delete'
    
    def get_publish_url(self):
        return f'{self.get_list_blogs_url()}{self.slug}/publish'

    def get_list_blogs_url(self):
        return '/blogs/'
