from django.contrib import admin
from django.urls import path
from dashboard_app import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('feedback/',views.Feedbackview,name='feedback'),
    path('myorders',views.Myorderview,name='my_order'),
    path('manage-order',views.Manageorder,name='manage-order'),
    path('update-order/<int:id>',views.UpdateOrder,name='update-order'),
    path('manage-user/', views.manage_user, name='manage_user'),
    path('user-details/<pk>', views.user_details, name='user_details'),
    path('delete-user/<pk>', views.delete_user, name='delete_user'),
    path('add-user/', views.add_user, name='add_user'),
    path('verified-user/', views.verified_user, name='verified_user'),

    path('add-slider/', views.add_slider, name='add_slider'),
    path('delete-img/<pk>/', views.delete_img, name='delete_img'),

    path('add-homepage-complete/', views.add_homepage_complete, name='home_page_complete'),
    path('delete-homepage-complete/<pk>/', views.delete_homepage_complete, name='delete_homepage_complete'),

    path('add-youcan-get/', views.add_youcan_get, name='youcan_get'),
    path('delete-youcan-get/<pk>/', views.delete_youcan_get, name='delete_youcan_get'),

    path('add-achivement/', views.add_achivement, name='add_achivement'),
    path('delte-achivement/<pk>/', views.delete_achivement, name='delete_achivement'),
    path('add-client-reveiw/', views.add_client_review, name='add_client_review'),

    path('add-footer-section/', views.add_footer_seciton, name='add_footer_section'),
    path('edit-footer-section/<pk>/', views.edit_footer_section, name='edit_footer_section'),

    path('profile/', views.profile, name='profile'),

    path('add-product/', views.add_product, name='add_product'),
    path('add-product-info/', views.add_product_info, name='add_product_info'),
    path('manage-product/', views.manage_product, name='manage_product'),
    path('delele-product/<pk>/', views.delete_product, name='delete_product'),
    path('edit-basic-product-info/<pk>/', views.edit_basic_product_info, name='edit_basic_product_info'),
    path('edit-standered-product-info/<pk>/', views.edit_standered_product_info, name='edit_standered_product_info'),
    path('edit-pro-product-info/<pk>/', views.edit_pro_product_info, name='edit_pro_product_info'),
    # path('edit-basic-product-info/<pk>/', views.edit_basic_product_info, name='edit_basic_product_info'),





]
