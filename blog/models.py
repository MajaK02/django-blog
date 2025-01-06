from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True) # a slug is a short name for an article that is still in production. It is used to identify the article in the database.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
) 
# One user can write many posts, so this is a one-to-many or Foreign Key. 
# The cascade on delete means that on the deletion of the user entry, all their posts are also deleted.
    content = models.TextField() # blog article content 
    created_on = models.DateTimeField(auto_now_add=True) # date and time the article was created/ The auto_now_add=True means the default created time is the time of post entry.
    status = models.IntegerField(choices=STATUS, default=0) # status of the article. 0 is draft, 1 is published.
    excerpt = models.TextField(blank=True) # a short description of the article.
    updated_on = models.DateTimeField(auto_now=True) # date and time the article was last updated.


# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

