from accounts.models import Profile
from blog_app.forms import CommentForm, PostForm
from django.db.models import Q, Count
from blog_app.models import Category, Comment, Post, PostViews
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required


'''
class PostsView(ListView):
    model = Post
    #queryset = Post.objects.all()
    template_name = 'post/posts.html'
    context_object_name ='posts' 
    paginate_by = 1

'''


def PostsView(request):
    posts=Post.objects.all()
    page_title="Posts"

    p = Paginator(posts, 2)#num of items per page
    page_number = request.GET.get('page')
    #page_obj = p.get_page(page_number)

    try:
        page_obj = p.page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)                  #if page number is not intger get the first page
    except EmptyPage:
        page_obj = p.page(p.num_pages)        #if page is empty get the last page


    context={
        'page_title' : page_title,
        'posts' : page_obj,
        }

    return  render(request, 'post/posts.html',context)



def PostsDetailsView(request,slug,):
    page_title="Post Content"
    post_details=Post.objects.get(slug=slug)
    replies=Comment.objects.filter(reply__isnull=False, )       # filter replies only not comments
    latest=Post.objects.all().order_by('-published_at')[0:3]  # the latest posts
    categories = Post.objects.values('categories__title','categories__slug').annotate(qcount=Count('categories')).order_by('-qcount') # To show how many posts per category and order_by the highest category in posts count (DESC)
                                            #↓
            #must be written like this because it is many_too_many field returns with ids not titles                   

    form = CommentForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            profile=Profile.objects.get(user=request.user)  # if i write it before form is valid it block anynomys users from entering the page
            form.instance.replier = profile        # check if the form is vaild give it the the logged in user profile
            form.instance.post = post_details      # and the post of the comment (both are model fields)
            form.save()
            return redirect(reverse('blog:post_details', args=(slug,))) # the way to redirect slug

    
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')      #to get IPAdress to count the post views
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

                   # to record  one view only per user for every post using his IPAdress
    PostViews.objects.get_or_create(IPAddres= get_client_ip(request) , post=post_details)
  
    context={
        'latest_posts' : latest,
        'post_details' : post_details,
        'categories'   : categories,
        'comment_form' : form,
        'replies'      : replies,
        'page_title'   : page_title,
        }
    return  render(request, 'post/post_details.html',context)




@login_required 
def create_post(request):
    page_title= "Create Post"
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            myfrom=form.save(commit=False)
            myfrom.author = request.user
            myfrom.save()
            form.save_m2m()                 # save many 2 many field must be like that
            return redirect(reverse('blog:posts'))
        else:
            form = PostForm()

    context={
        'create_or_update_post_form' : form,
        'page_title'                 : page_title,
    }
    return render(request, 'post/post_create_or_update.html',context)



@login_required 
def post_update(request,slug):                  #the same view and template create_post with minor change "instance=post_details" 
    page_title= "Edit Post"
    post_details=Post.objects.get(slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post_details) # use "instance=" to give the form the current data in the form
    if request.method == "POST":
        if form.is_valid():
            myfrom=form.save(commit=False)
            myfrom.save()
            form.save_m2m()                 # save many 2 many field must be like that
            return redirect(reverse('blog:post_details', args=(slug,)))  # the way to redirect slug
        else:
            form = PostForm()

    context={
        'create_or_update_post_form' : form,
        'page_title'                 : page_title,
    }
    return render(request, 'post/post_create_or_update.html', context)     # different urls for the same html page



@login_required 
def post_delete(request,slug):
    post_details=Post.objects.get(slug=slug)
    if request.method=="POST":
        post_details.delete()
        return redirect(reverse('blog:posts'))
    return render(request,'post/post_details.html',)



@login_required
def comment_update(request, slug, id):
    comment=Comment.objects.get(id=id)        
    form = CommentForm(request.POST or None, request.FILES or None, instance=comment)
    if request.method == "POST":
        if form.is_valid(): 
            form.save()
            return redirect(reverse('blog:post_details', args=(slug,))) # the way to redirect slug
        else:
            form = CommentForm()

    context={
        'comment_update_form' : form,
        }
    return  render(request, 'post/comment_update.html',context)


@login_required
def comment_delete(request, slug, id):
    comment=Comment.objects.get(id=id)
    if request.method == "POST":
        comment.delete()
        return redirect(reverse('blog:post_details', args=(slug,))) # the way to redirect slug
    return render(request,'post/post_details.html',)



@login_required
def reply_create(request, slug, id,):   #create first reply
    page_title="Create reply"
    post_details=Post.objects.get(slug=slug)
    reply_to=Comment.objects.get(id=id)     #reply to comment
    form=CommentForm(request.POST or None, request.FILES or None, initial={'content':'@[{0}]'.format(reply_to.replier)})
    if request.method=='POST':                                    #to mention the replied_to person in the reply (facebook like)
        if form.is_valid:
            profile=Profile.objects.get(user=request.user)
            form.instance.replier=profile
            form.instance.post=post_details
            form.instance.reply=reply_to
            form.save()
            return redirect(reverse('blog:post_details', args=(slug,))) # the way to redirect slug
        else:
            form = CommentForm()

    context={
        'reply_create_form' : form,
        'page_title'        :page_title,
        }
    return  render(request, 'post/reply_create.html',context)


@login_required
def reply_to_reply_create(request, slug, id, pk):   #create the nested replies
    page_title="Create reply"
    post_details=Post.objects.get(slug=slug)
    reply_to=Comment.objects.get(id=id)        #reply to comment, to show it as the first reply down to comment (facebook like)
    reply_to_reply=Comment.objects.get(id=pk)  #the mentioned reply  
    form=CommentForm(request.POST or None, request.FILES or None, initial={'content':'@[{0}]'.format(reply_to_reply.replier)})
    if request.method=='POST':                                    #to mention the replied_to person in the reply (facebook like)
        if form.is_valid:
            profile=Profile.objects.get(user=request.user)
            form.instance.replier=profile
            form.instance.post=post_details
            form.instance.reply=reply_to
            form.save()
            
            return redirect(reverse('blog:post_details', args=(slug,))) # the way to redirect slug
        else:
            form = CommentForm()
    
    context={
        'reply_create_form' : form,
        'page_title'        :page_title,
        }
    return  render(request, 'post/reply_create.html',context)


def search_view(request):
    search = Post.objects.all()
    page_title=" Blog Search Results"
    query = request.GET.get('q')                #the search text
    if query:
        search = search.filter(
            Q(title__icontains=query) |             # filter with containing in title, description or content 
            Q(description__icontains=query) |
            Q(content__icontains=query)
        ).distinct()                                # don't repeat the results

    p = Paginator(search, 1)#num of items per page
    page_number = request.GET.get('page')
    try:
        page_obj = p.page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)                  #if page number is not intger get the first page
    except EmptyPage:
        page_obj = p.page(p.num_pages)        #if page is empty get the last page

    context={
        'search_results': page_obj,
        "query"         : query,
        'page_title'    : page_title,                   
    }
    return  render(request, 'post/posts_search.html',context)


@login_required
def like_or_unlike(request,slug):
    post = Post.objects.get(slug=slug)

    if request.user in post.likes.all():               # unlike or like depending if the user liked or not
        post.likes.remove(request.user)
        
        return redirect(reverse('blog:post_details', args=(slug,)))
    else:
        post.likes.add(request.user)

        return redirect(reverse('blog:post_details', args=(slug,)))



def category_posts(request, slug):
    page_title="Post Category"
    category= Category.objects.get(slug=slug)
    category_posts=category.posts.all()         #posts is a related name in models/Post/categories

    p = Paginator(category_posts, 1)#num of items per page
    page_number = request.GET.get('page')
    #page_obj = p.get_page(page_number)

    try:
        page_obj = p.page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)                  #if page number is not intger get the first page
    except EmptyPage:
        page_obj = p.page(p.num_pages)        #if page is empty get the last page


    context={
        'page_title' : page_title,
        'category'   : category,
        'category_posts' : page_obj,
    }

    return  render(request, 'post/category_posts.html',context)