from django.urls import path
from .views import PostList, PostDetail, Search, PostAdd, PostUpgrade, PostDelete, Accept, Cans, UserView

urlpatterns = [
    path('', PostList.as_view(), name='index'),
    path('<int:pk>', PostDetail.as_view(), name='board'),
    path('search/', Search.as_view(), name='search_results'),
    path('add/', PostAdd.as_view(), name='add'),
    path('<int:pk>/edit', PostUpgrade.as_view(), name='edit'),
    path('<int:pk>/delete', PostDelete.as_view(), name='delete'),
    path('profile/', UserView.as_view(), name='profile'),
    path('accept/<int:pk>/', Accept.as_view(), name='accept'),
    path('cancel/<int:pk>/', Cans.as_view(), name='cancel'),

    ]