from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import ContactMessage
from .serializers import ContactSerializer


class ContactViewSet(ModelViewSet):

    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            {
                "success": True,
                "message": "Contact message submitted successfully.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )