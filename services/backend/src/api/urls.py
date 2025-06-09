from django.urls import path
from . import views

urlpatterns = [
    path('results/', views.ResultsData.as_view(), name='results-data'),
]
