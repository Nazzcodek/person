from django.urls import path, re_path
from person_api import views

urlpatterns = [
	path('', views.ApiOverview, name='home'),
    path('create/', views.add_person, name='add-person'),
    path('all/', views.view_persons, name='view_persons'),
    path('update/<int:pk>/', views.update_person, name='update_person'),
    path('person/<int:pk>/delete/', views.delete_person, name='delete-person'),
   
]
