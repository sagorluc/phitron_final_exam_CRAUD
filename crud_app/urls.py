from django.urls import path
from crud_app.views import show_crud, create_crud, update_crud, delete_crud,\
more_info, search_item, home

urlpatterns = [
    path('', home, name='home'),
    path('show_crud/', show_crud, name='show_crud'),
    path('create/', create_crud, name='create_post'),
    path('update/<int:id>/', update_crud, name='update_crud'),
    path('delete/<int:id>/', delete_crud, name='delete_crud'),
    path('info/<int:id>/', more_info, name='more_info'),
    path('search', search_item, name='search'),
    # path('profile/<int:id>/', profile_update, name='profile'),
]
