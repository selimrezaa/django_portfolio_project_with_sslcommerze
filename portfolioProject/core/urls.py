from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.home_view,name='home'),

    path('works', views.works_view,name='works'),
    path('contactus', views.contactus_view,name='contactus'),
    path('teams', views.teams_view,name='teams'),
    path('aboutus', views.aboutus_view,name='aboutus'),
    # path('signup', views.clientaccountsignup_view,name='signup'),
    # path('signin', views.clientaccountsignin_view,name='signin'),
    # path('myaccount', views.myaccount_view,name='myaccount'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
