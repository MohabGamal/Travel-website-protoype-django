from django.urls import path
from . import views



app_name='blog_app'


urlpatterns = [
    path('', views.posts, name='posts'),
    path('post/create/', views.create_post, name='post_create'),
    path('category_posts/<str:slug>', views.category_posts, name='category_posts'),
    path('<str:slug>/', views.PostsDetailsView, name='post_details'),
    path('<str:slug>/update', views.post_update, name='post_update'),
    path('<str:slug>/delete', views.post_delete, name='post_delete'),
    path('<str:slug>/like_or_unlike/', views.like_or_unlike, name='like_or_unlike'),
    path('<str:slug>/<int:id>/comment_update', views.comment_update, name='comment_update'),
    path('<str:slug>/<int:id>/comment_delete', views.comment_delete , name='comment_delete'),
    path('<str:slug>/<int:id>/reply_create'  , views.reply_create , name='reply_create'),
    path('<str:slug>/<int:id>/<int:pk>/reply_to_reply_create'  , views.reply_to_reply_create , name='reply_to_reply_create'),
        #post_deatils #comment #reply
    
    #slug must be the last path in case i have an url matchs with slug the browser will go to the url not the slug
    
    

]