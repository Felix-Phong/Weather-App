from django.urls import path
from . import views # call to url_shortener/views.py

urlpatterns = [
    path('', views.index, name='index'),
    path('PredictByTime/',views.PDByTime,name='Predict_By_Time'),
     path('PredictByDate/',views.PDByDate,name='Predict_By_Date'),
]