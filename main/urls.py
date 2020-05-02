from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all, name = 'all'),
    path('published/', views.published, name = 'published'),
    path('drafts/' , views.drafts, name = 'drafts'),
    path('deleted/', views.deleted, name = 'deleted'),
]