from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('library', views.LibraryHome, name='library'),
    path('delete-book/<int:id>', views.DeleteBook, name='delete-book'),
    path('update-book/<int:id>', views.UpdateBook, name="update-book"),
]