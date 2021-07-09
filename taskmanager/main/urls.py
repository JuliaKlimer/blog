from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('add', views.add, name='add'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete')
]