from django.urls import path

from .views import lan_fw, lan_info, fw_info

urlpatterns = [
    path('languages/', lan_fw, name='languages'),
    path('languages/<int:pk>', lan_info, name='lan_url'),
    path('languages/fw/<int:pk>', fw_info, name='fw_url'),
]