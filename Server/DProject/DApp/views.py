from django.shortcuts import render
from .models import Member
from .serializer import memberSerializer

# Create your views here.
@api_view(('GET'))
def get_member(request):
    member = Member.objects.all()
    SerializerData = memberSerializer(member, many=True).data
    return Response(serializer.data)

@api_view(('POST'))
def create_member(request):
    member = request.data
    serializer = memberSerializer(data=member)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)