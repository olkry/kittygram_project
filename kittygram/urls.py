from django.urls import path

from cats.views import cat_list, hello, cat_detail

urlpatterns = [
   path('cats/<int:pk>/', cat_detail),
   path('cats/', cat_list),
   path('hello/', hello),
]


