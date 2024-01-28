from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

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

    class Meta:
        ordering = ['-publish_date','-updated','-timestamp']

    def get_retrieve_url(self):
        return f'/blogs/retrieve/{self.slug}'
    
    def get_edit_url(self):
        return f'/blogs/{self.slug}/edit'
    
    def get_delete_url(self):
        return f'/blogs/{self.slug}/delete'

    def get_list_blogs_url(self):
        return '/blogs/'
