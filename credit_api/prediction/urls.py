from django.urls import path
from .views import predict_creditworthiness

urlpatterns = [
  path("predict/", predict_creditworthiness, name="predict_creditworthiness"),
]
