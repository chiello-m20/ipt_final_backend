from django.urls import path
from .views import MotionEventListCreateAPIView, ClearMotionEventsAPIView

urlpatterns = [
    path('motion-events/', MotionEventListCreateAPIView.as_view(), name='motion-events'),
    path('motion-events/clear/', ClearMotionEventsAPIView.as_view(), name='clear-motion-events'),  # ← added this
]
