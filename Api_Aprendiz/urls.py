from django.urls import path
from .views import AprendicesViews

urlpatterns = [
    path('aprendices/', AprendicesViews.as_view(), name='lista_aprendices'),
    path('aprendices/<int:id>', AprendicesViews.as_view())
]
