from accounts.models import Profile
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from martor.models import MartorField 
from django.db.models import Count



class Post(models.Model):
    title = models.CharField(max_length=100, unique= True)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(User, on_delete=models.CASCADE)   # it is better to be related to Profile to acsess more info about the user  (next time xD)
    categories = models.ManyToManyField('Category', blank=False, related_name="posts")
    post_cover = models.ImageField(upload_to='Posts')                   #related_name to get the posts of this category
    slug= models.SlugField(blank=True, null=True, unique=True)
    likes= models.ManyToManyField(User, blank=True, related_name="likes")
    content = MartorField()               # must be the last to write down to it hints
                                                                   


    def save(self,*args, **kwargs):              #overriding save method 
        self.slug= slugify(self.title)           #create a slug
        super(Post,self).save(*args,**kwargs)

    def __str__(self):
        return self.title


    @property
    def get_comments(self):                  # property to relate between post and comments so comments appear only in post page and i can call get_comments as a field in Post. Also, if i delete post i delete its comments. Must also give related_name in comment class
        
        return self.comments.filter(reply__isnull=True,).order_by('-commented_at')        #for more https://stackoverflow.com/questions/58558989/what-does-djangos-property-do
                                    # filter the comments only not replies
    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    @property                                # property so if i delete post i delete its views
    def views_count(self):                   # to recored views count
        return PostViews.objects.filter(post=self).count()
    


class Comment(models.Model):
    commented_at = models.DateTimeField(auto_now_add=True)
    content= MartorField()
    replier= models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    post=models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    reply=models.ForeignKey('Comment', on_delete=models.CASCADE, related_name="replies", null=True, blank=True,)
      # recursive relationship for replies 


class PostViews(models.Model):                              # to recored views count
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    IPAddres= models.GenericIPAddressField(default="45.243.82.162")
    
    def __str__(self):
        return '{0}'.format(self.IPAddres)



class Category(models.Model):
    title = models.CharField(max_length=20)
    slug  = models.SlugField(blank=True, null=True, unique=True)

    def save(self,*args, **kwargs):              #overriding save method 
        self.slug= slugify(self.title)           #create a slug
        super(Category,self).save(*args,**kwargs)
  
    def __str__(self):
        return self.title

