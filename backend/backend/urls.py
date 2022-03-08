
from django.contrib import admin
from django.urls import path
from geodata.views import geodata_list_view,geodata_create_apiview,geodata_approve_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',geodata_list_view,name="geodata_list_view"),
    path('api/geodata/',geodata_create_apiview,name="geodata_create_apiview"),
    path('approve/<int:id>',geodata_approve_view,name="geodata_approve_view")
]
