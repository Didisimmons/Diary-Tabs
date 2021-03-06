from django.urls import path
from . import views

urlpatterns = [
    path('', views.entryList, name="home"),
    path('entryDetailView/<int:entry_id>', views.entryDetailView, 
         name='detail_view'),
    path('editDetailView/<int:entry_id>/', views.editDetailView,
         name='edit_events'),
]
