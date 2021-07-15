from django.urls import path
from . import views

urlpatterns = [
    path('', views.show),
    path('show/new', views.new),
    path('show/create_show', views.create_show),
    path('show/<int:id>', views.one_show),
    path('show/<int:id>/edit', views.edit_show),
    path('show/<int:id>/update', views.update_show),
    path('show/<int:id>/delete', views.delete_show),
]
