from django.urls import path
from .views import CompanyView, DeveloperView

urlpatterns = [
    path('companies/', CompanyView.as_view(), name='company_list'),
    path('companies/<int:id>', CompanyView.as_view()),
    path('developers', DeveloperView.as_view()),
    path('developers/<int:id>', DeveloperView.as_view()),
]
