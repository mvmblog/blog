from django.db import models

STATUS = (
    (0,'Draft'),
    (1,'Publish')
)


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    class_and_section = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title