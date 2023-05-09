from django.db import models

class PostManager(models.Manager):
    def get_queryset(self):
        return super(PostManager,self).get_queryset().filter(post_types = "post")


class LinkManager(models.Manager):
    def get_queryset(self):
        return super(LinkManager,self).get_queryset().filter(post_type = "link")
