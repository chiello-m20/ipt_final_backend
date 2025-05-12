from django.db import models

class MotionEvent(models.Model):
    device_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    alert_message = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.device_name} - {self.timestamp}"
