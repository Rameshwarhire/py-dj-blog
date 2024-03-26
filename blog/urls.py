from django.urls import path
from . import views

urlpatterns =[
    path('',views.PostListView.as_view(),name="blog-home"),
    path('post/<int:pk>',views.PostDetailView.as_view(),name="post-detail"),
    path('create',views.PostCreateView.as_view(),name="create-post"),
    path('update/<int:pk>',views.PostUpdateView.as_view(),name="update-post"),
    path('delete/<int:pk>',views.PostDeleteView.as_view(),name="delete-post"),
]
