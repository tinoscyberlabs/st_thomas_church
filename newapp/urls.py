"""
URL configuration for churchpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('admin_base',views.admin_base,name='admin_base'),
    path('login_user',views.login_user,name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('about',views.about,name='about'),
    path('Event_Details/<str:event_name>/',views.Event_Details,name='Event_Details'),
    path('admin_add_events',views.admin_add_events,name='admin_add_events'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('bishop_message',views.bishop_message,name='bishop_message'),
    path('vicar_message',views.vicar_message,name='vicar_message'),
    path('image_shadow',views.image_shadow,name='image_shadow'),
    path('admin_event_view',views.admin_event_view,name='admin_event_view'),
    path('admin_delete_events/<int:id>', views.admin_delete_events, name='admin_delete_events'),
    path('admin_update_events/<int:id>',views.admin_update_events,name='admin_update_events'),
    path('january',views.january,name='january'),
    path('february',views.february,name='february'),
    path('march',views.march,name='march'),
    path('april',views.april,name='april'),
    path('may',views.may,name='may'),
    path('june',views.june,name='june'),
    path('july',views.july,name='july'),
    path('auguest',views.auguest,name='auguest'),
    path('september',views.september,name='september'),
    path('october',views.october,name='october'),
    path('november',views.november,name='november'),
    path('december',views.december,name='december'),
   

    path('admin_add_ministries',views.admin_add_ministries,name='admin_add_ministries'),
    path('admin_ministries_view',views.admin_ministries_view,name='admin_ministries_view'),
    path('admin_update_ministries/<int:id>',views.admin_update_ministries,name='admin_update_ministries'),
    path('admin_delete_ministries/<int:id>',views.admin_delete_ministries,name='admin_delete_ministries'),

    path('mass_times',views.mass_times,name='mass_times'),
    path('admin_add_mass_times',views.admin_add_mass_times,name='admin_add_mass_times'),
    path('admin_daily_mass_view',views.admin_daily_mass_view,name='admin_daily_mass_view'),
    path('admin_update_mass_times/<int:id>',views.admin_update_mass_times,name='admin_update_mass_times'),
    path('admin_delete_mass_times/<int:id>',views.admin_delete_mass_times,name='admin_delete_mass_times'),
    

    path('admin_add_special_masses',views.admin_add_special_masses,name='admin_add_special_masses'),
    path('admin_special_mass_view',views.admin_special_mass_view,name='admin_special_mass_view'),
    path('admin_update_special_mass/<int:id>',views.admin_update_special_mass,name='admin_update_special_mass'),
    path('admin_delete_special_mass/<int:id>',views.admin_delete_special_mass,name='admin_delete_special_mass'),

    path('obituary',views.obituary,name='obituary'),
    path('admin_add_obituary',views.admin_add_obituary,name='admin_add_obituary'),
    path('admin_update_obituary/<int:id>',views.admin_update_obituary,name='admin_update_obituary'),
    path('admin_delete_obituary/<int:id>',views.admin_delete_obituary,name='admin_delete_obituary'),
    path('admin_obituary_view',views.admin_obituary_view,name='admin_obituary_view'),

    # path('gallery/<int:id>',views.gallery,name='gallery'),
    path('admin_add_gallery',views.admin_add_gallery,name='admin_add_gallery'),
    path('admin_gallery_view',views.admin_gallery_view,name='admin_gallery_view'),
    path('admin_update_gallery/<str:gallery_name>/',views.admin_update_gallery,name='admin_update_gallery'),
    path('admin_delete_gallery/<int:id>/',views.admin_delete_gallery,name='admin_delete_gallery'),


    path('blog_single',views.blog_single,name='blog_single'),
    path('admin_add_blog',views.admin_add_blog,name='admin_add_blog'),
    path('admin_blog_view',views.admin_blog_view,name='admin_blog_view'),
    path('admin_update_blog/<int:id>',views.admin_update_blog,name='admin_update_blog'),
    path('admin_delete_blog/<int:id>',views.admin_delete_blog,name='admin_delete_blog'),
    path('blog', views.blog, name='blog'),
    
    path('test', views.test, name='test'),

    
    path('contact', views.contact, name='contact'),
    path('admin_delete_contacts/<int:id>',views.admin_delete_contacts,name='admin_delete_contacts'),
    path('admin_contact_view',views.admin_contact_view,name='admin_contact_view'),
    path('gallery_details/<str:name>/',views.gallery_details,name='gallery_details'),
    path('gallery',views.gallery,name='gallery'),
    path('admin_add_category',views.admin_add_category,name='admin_add_category'),
    path('admin_add_main_gallery',views.admin_add_main_gallery,name='admin_add_main_gallery'),
    path('admin_category_view',views.admin_category_view,name='admin_category_view'),
    path('admin_update_category/<str:name>/',views.admin_update_category,name='admin_update_category'),
    path('admin_delete_category<int:id>/',views.admin_delete_category,name='admin_delete_category'),
    path('admin_main_gallery_view',views.admin_main_gallery_view,name='admin_main_gallery_view'),
    path('admin_update_main_gallery/<int:id>/',views.admin_update_main_gallery,name='admin_update_main_gallery'),

    path('parishes',views.parishes,name='parishes'),
    path('eucharistic',views.eucharistic,name='eucharistic'),

    path('administration',views.administration,name='administration'),
    path('former_vicar',views.former_vicar,name='former_vicar'),
    path('former_asst_vicar',views.former_asst_vicar,name='former_asst_vicar'),
    path('former_trustees',views.former_trustees,name='former_trustees'),
    path('wards',views.wards,name='wards'),

    path('st_vincent_de_paul_society',views.st_vincent_de_paul_society,name='st_vincent_de_paul_society'),
    path('st_vincent_association',views.st_vincent_association,name='st_vincent_association'),
    path('st_vincent_association_view',views.st_vincent_association_view,name='st_vincent_association_view'),
    path('st_vincent_association_updation/<int:id>/',views.st_vincent_association_updation,name='st_vincent_association_updation'),
    path('st_vincent_association_delete/<int:id>/',views.st_vincent_association_delete,name='st_vincent_association_delete'),

    path('stars_pithruvedi', views.stars_pithruvedi,name='stars_pithruvedi'),
    path('stars_pithruvedi_association',views.stars_pithruvedi_association,name='stars_pithruvedi_association'),
    path('stars_pithruvedi_view',views.stars_pithruvedi_view,name='stars_pithruvedi_view'),
    path('stars_pithruvedi_updation/<int:id>/',views.stars_pithruvedi_updation,name='stars_pithruvedi_updation'),
    path('stars_pithruvedi_delete/<int:id>/',views.stars_pithruvedi_delete,name='stars_pithruvedi_delete'),

    path('mathru_jyothi', views.mathru_jyothi,name='mathru_jyothi'),
    path('mathru_jyothi_association',views.mathru_jyothi_association,name='mathru_jyothi_association'),
    path('mathru_jyothi_view',views.mathru_jyothi_view,name='mathru_jyothi_view'),
    path('mathru_jyothi_updation/<int:id>/',views.mathru_jyothi_updation,name='mathru_jyothi_updation'),
    path('mathru_jyothi_delete/<int:id>/',views.mathru_jyothi_delete,name='mathru_jyothi_delete'),

    path('styf', views.styf, name='styf'),
    path('styf_association',views.styf_association,name='styf_association'),
    path('styf_association_view',views.styf_association_view,name='styf_association_view'),
    path('styf_association_updation/<int:id>/',views.styf_association_updation,name='styf_association_updation'),
    path('styf_association_delete/<int:id>/',views.styf_association_delete,name='styf_association_delete'),

    path('error',views.error,name='error'),
    path('catechism',views.catechism,name='catechism'),

    path('UserRegister',views.UserRegister,name='UserRegister'),
    path('user_home',views.user_home,name='user_home'),
    path('st_vincent_home',views.st_vincent_home,name='st_vincent_home'),
    path('stars_pithrivedhi_home',views.stars_pithrivedhi_home,name='stars_pithrivedhi_home'),
    path('mathru_jyothi_home',views.mathru_jyothi_home,name='mathru_jyothi_home'),
    path('styf_home',views.styf_home,name='styf_home'),
    path('altar_servents_home',views.altar_servents_home,name='altar_servents_home'),
    path('bible_readers_home',views.bible_readers_home,name='bible_readers_home'),
    path('choir_home',views.choir_home,name='choir_home'),
    path('CML_home',views.CML_home,name='CML_home'),
    path('holy_childhood_home',views.holy_childhood_home,name='holy_childhood_home'),
    path('UserLogin',views.UserLogin,name='UserLogin'),
    path('auditorium_booking',views.auditorium_booking,name='auditorium_booking'),
    path('admin_booking_view',views.admin_booking_view,name='admin_booking_view'),
    path('admin_delete_booking/<int:id>/',views.admin_delete_booking,name='admin_delete_booking'),

    path('admin_registration_view',views.admin_registration_view,name='admin_registration_view'),
    path('admin_registration_delete/<int:id>/',views.admin_registration_delete,name='admin_registration_delete'),

    path('blog_single',views.blog_single,name='blog_single'),
]

   




