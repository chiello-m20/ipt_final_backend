from django.urls import path
from .views import MotionEventListCreateAPIView

urlpatterns = [
    path('motion-events/', MotionEventListCreateAPIView.as_view(), name='motion-events'),
]
