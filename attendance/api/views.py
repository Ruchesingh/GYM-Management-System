from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from attendance.api.serializer import AttendanceSerializer
from attendance.models import Attendance

class AttendanceView(GenericAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def patch(self,request,*args, **kwargs):
        print(kwargs)
        return Response({
            "message":"Patch request"
        })