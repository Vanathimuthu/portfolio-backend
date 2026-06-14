from django.conf import settings
from django.core.mail import send_mail
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

        contact_message = serializer.save()

        body = (
            f"Name: {contact_message.name}\n"
            f"Email: {contact_message.email}\n\n"
            f"Message:\n{contact_message.message}"
        )

        try:
            send_mail(
                subject="Portfolio Contact Message",
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            print("EMAIL SENT SUCCESSFULLY")

        except Exception as e:
            print("EMAIL ERROR:", str(e))

        return Response(
            {
                "success": True,
                "message": "Contact message submitted successfully.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )