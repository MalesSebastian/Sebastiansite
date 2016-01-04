from django.db import models
import uuid
from django.core.urlresolvers import reverse

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)


class Post(models.Model):
    title = models.CharField(max_length=100, default='')
    text = models.TextField(default='')
    slug = models.SlugField(default=uuid.uuid1, unique=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='w')
    description = models.TextField(default='', max_length=300)
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)

    def get_absolute_url(self):
        return reverse('post', args=[self.slug])

    def __unicode__(self):
        return self.title

    def edit_text(self, text):
        self.text = text

    class Meta:
        get_latest_by = 'creation_date'


class Comment(models.Model):
    post_at = models.ForeignKey(Post, related_name="comments")
    submitter = models.TextField(default='', max_length=20)
    text = models.CharField(default='', max_length=200)
