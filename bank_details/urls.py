from django.urls import path
from .views import *

urlpatterns = [
    path('branches/', get_branches, name='branch-list'),
    path('branches/<str:ifsc_code>', get_branch, name='branch-detail'),
    path('branches/create/', create_branch, name='branch-create'),
    path('bank/', get_bank , name='get-bank'),
    path('add_bank/', create_bank, name='create_bank')
]
