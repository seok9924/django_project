from django.urls import path
from  . import views



urlpatterns=[
    path('blog/',views.PostList.as_view()),
    path('blog/<int:pk>/',views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    path('blog/category/<str:slug>/',views.category_page),
    path('blog/create_post/',views.PostCreate.as_view()),
    path('blog/update_post/<int:pk>/',views.PostUpdate.as_view()),
    path('blog/tag/<str:slug>/',views.tag_page),
]