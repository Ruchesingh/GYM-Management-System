
from member.models import Member
from member.api.serializer import MemberSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def memberlist(request):
    data = Member.objects.all()
    serializer  = MemberSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def membercreate(request):
    post_data = request.data
    serializer = MemberSerializer(data=post_data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"Member Successfully created"
        },201)
    else:
        return Response(serializer.errors,422)
