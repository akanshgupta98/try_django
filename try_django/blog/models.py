from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,default=1)
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(blank=True, auto_now = True)
    slug = models.SlugField(default = "hello-world",unique=True)

    def get_retrieve_url(self):
        return f'/blogs/retrieve/{self.slug}'
    
    def get_edit_url(self):
        return f'/blogs/{self.slug}/edit'
    
    def get_delete_url(self):
        return f'/blogs/{self.slug}/delete'
