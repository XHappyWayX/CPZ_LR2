from django.urls import path
from .views import *

urlpatterns = [
    path('api/', CheckRequestInDB.as_view(), name='Request'),
]