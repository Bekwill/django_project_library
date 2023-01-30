from django.urls import path
from library.views import author

urlpatterns = [
    path('authors/create', author.create, name='author-create'),
    path('authors/', author.list_all, name='author-list'),
    path('authors/<int:pk>/', author.detail,name='author-detail'),
    path('authors/<int:pk>/update/', author.update, name='author-update'),
    path('authors/<int:pk>/delete/', author.delete , name='author-delete'),

]