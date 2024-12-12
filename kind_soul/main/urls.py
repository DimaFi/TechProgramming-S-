from django.urls import path
from . import views
from .views import TopicListView, TopicDetailView, TopicCreateView, CommentCreateView

from .views import register_view, login_view
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index_view, name='index'),
    path('news/', views.news_view, name='news'),
    path('animals/', views.animals_view, name='animals'),

    # forum
    path('forum/', TopicListView.as_view(), name='topic-list'),
    path('forum/topic/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    path('forum/topic/new/', TopicCreateView.as_view(), name='topic-create'),
    path('forum/topic/<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),  # Создание комментария
    
    # register
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
