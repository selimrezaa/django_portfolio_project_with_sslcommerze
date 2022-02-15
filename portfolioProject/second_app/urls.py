from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from second_app import views

urlpatterns = [
        path('', views.index, name='index'),
        path('service/', views.service, name='service'),
        path('signup/', views.sign_up, name='signup'),
        path('login/', views.user_login, name='login'),
        path('logout/', views.user_logout, name='logout'),
        #email varifications
        path('password-reset/', views.PasswordResetView.as_view(template_name='first_app/passwordreset.html'), name='password_reset'),
        path('password-reset-done/', views.PasswordResetDoneView.as_view(template_name='first_app/password_reset.html'), name='password_reset_done'),
        path('rest/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='first_app/passwordresetconfirm.html'), name='password_reset_confirm'),
        path('password-reset-complete/', views.PasswordResetCompleteView.as_view(template_name='first_app/passwordresetcomplete.html'), name='password_reset_complete'),
        path('activate/<uidb64>/<token>/', views.activate, name='activate'),


        path('work/', views.our_work, name='our_work'),
        path('team-member/', views.team_member, name='team_member'),
        path('about-us/', views.about_us, name='about_us'),
        path('test2/', views.test2),

        path('checkout/<int:service_id>/<int:package_id>', views.checkout, name="checkout"),
        path('pay/<int:id>', views.payment, name="payment"),
        path('status/', views.complete, name="complete"),
        path('purchase/<val_id>/<tran_id>/', views.purchase, name="purchase"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
