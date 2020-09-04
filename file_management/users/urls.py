from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
# from users import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^upload_video/$', views.upload_video, name='upload_video'),
    url(r'^get-frames/$', views.get_frames, name='get-frames'),
    url(r'^get_circle/$', views.get_circle, name='get_circle'),
    url(r'^get_shape/$', views.get_shape, name='get_shape'),
    # url(r'^register/$', views.register, name='register'),
    # url(r'^forgot_password/$', views.forgot_password, name='forgot_password'),
    # url(r'^logout/$', views.userLogout, name='logout'),
    # url(r'^password_reset/([0-9A-Za-z]{1,8}-[0-9A-Za-z]{1,4}-[0-9A-Za-z]{1,4}-[0-9A-Za-z]{1,4}-[0-9A-Za-z]{1,12})/$',views.password_reset,name='password_reset'),
    # url(r'^password_reset/$',views.password_reset,name='password_reset'),
    # url(r'^password_reset/(?P<token>[-\w]+)/$', views.password_reset, name='password_reset'),
    # url(r'^activate-account/(?P<token>[-\w]+)/$', views.activate_account, name='activate-account'),
    # url(r'^update_password_reset/$', views.update_password_reset, name='update_password_reset'),
    # url(r'^user-profile/$', views.updateUserProfile, name='user-profile'),
    # url(r'^update_profile_image/$', views.updateUserProfileImage, name='user-profile-image'),
    # url(r'^my-wishlist/$', views.myWishlist, name='myWishlist'),
    # url(r'^change-password/$', views.changePassword, name='changePassword'),
    # url(r'toc_register/$', views.toc_register, name='toc_register'),
    # url(r'^updateProfile/$', views.updateProfile, name='updateProfile'),
]

# handler404 = file_management.page.views.handler404
# handler500 = file_management.page.views.handler500