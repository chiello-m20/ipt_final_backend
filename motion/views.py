from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MotionEvent
from .serializers import MotionEventSerializer

# List & Create View
class MotionEventListCreateAPIView(generics.ListCreateAPIView):
    queryset = MotionEvent.objects.all().order_by('-timestamp')
    serializer_class = MotionEventSerializer

# New View to Clear All Events
class ClearMotionEventsAPIView(APIView):
    def delete(self, request):
        MotionEvent.objects.all().delete()
        return Response({"message": "All motion events cleared."}, status=status.HTTP_204_NO_CONTENT)
