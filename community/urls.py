from django.urls import path
from .views import post_create, delete_post, PostDetailView, save_comment, scrab_post, delete_comment, load_scrab_list, redirect_scrab_detail, delete_scrab, my_post, search_post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post/', post_create, name='post_create'),
    path('post_delete/', delete_post, name = 'delete_user'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('save_comment/', save_comment, name = 'save_comment'),
    path('delete_comment/', delete_comment, name = 'delete_comment'),
    path('post/scrab/', scrab_post, name = 'post_load'),
    path('my_page/scrab_post/', load_scrab_list, name = 'load_scrab'),
    path('redirect_to_post/<int:post_id>/', redirect_scrab_detail, name = 'redirect_scrab_detail'),
    path('delete_scrab/', delete_scrab, name = 'delete_scrab'),
    path('my_post/', my_post, name = 'my_post'),
    path('search_post/', search_post, name = 'my_post'),
    # path('revise_post', revise_post)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)