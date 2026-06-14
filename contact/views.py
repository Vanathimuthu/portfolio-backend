from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import ContactMessage
from .serializers import ContactSerializer


class ContactViewSet(
    ModelViewSet
):

    queryset = (
        ContactMessage.objects.all()
    )

    serializer_class = (
        ContactSerializer
    )

    def create(
        self,
        request,
        *args,
        **kwargs
    ):

        serializer = (
            self.get_serializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        contact_message = serializer.save()
        sender_email = contact_message.email
        body = (
            f"Name: {contact_message.name}\n"
            f"Email: {sender_email}\n\n"
            f"Message:\n{contact_message.message}"
        )

        try:
            send_mail(
                "Portfolio Contact",
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
        except Exception as e:
            print("EMAIL ERROR:", str(e))

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )