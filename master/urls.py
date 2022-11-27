
from django.urls import path

from . import views


urlpatterns = [
   path('',views.home,name='home'),
   path('prot',views.protfolio,name='prot'),
   path('prot_detial/<pk>',views.protfolio_detial,name="prot_detial"),
   path('blog',views.blog,name='blog'),
   path('blog_detail/<pk>',views.blog_detail,name='blog_detail'),
   path('team',views.team,name='team'),
   path('contact',views.contact_view,name="contact"),
   path('sub',views.sub_view,name='sub'),

]