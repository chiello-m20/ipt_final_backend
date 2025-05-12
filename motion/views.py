from rest_framework import generics
from .models import MotionEvent
from .serializers import MotionEventSerializer

class MotionEventListCreateAPIView(generics.ListCreateAPIView):
    queryset = MotionEvent.objects.all().order_by('-timestamp')
    serializer_class = MotionEventSerializer
