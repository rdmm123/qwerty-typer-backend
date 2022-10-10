from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from apps.qwerty_core.models import Text
from apps.qwerty_core.serializers import TextSerializer


class RandomText(APIView):
    def get(self, request, format=None):
        lang = request.query_params.get('lang', None)

        if lang not in settings.ALLOWED_LANGUAGES:
            return Response({'error': 'Invalid language'}, status=status.HTTP_400_BAD_REQUEST)

        if not lang:
            return Response({'error': 'Must specify a language'}, status=status.HTTP_400_BAD_REQUEST)

        try: 
            text = Text.objects.get_random_text(lang)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TextSerializer(text)
        return Response(serializer.data)


class AllowedLanguages(APIView):
    
    def get(self, request, format=None):
        return Response(settings.ALLOWED_LANGUAGES)