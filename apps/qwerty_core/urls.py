from django.urls import path
from apps.qwerty_core.views import AllowedLanguages, RandomText

urlpatterns = [
    path('random-text/', RandomText.as_view(), name='random_text'),
    path('languages/', AllowedLanguages.as_view(), name='languages'),
]
