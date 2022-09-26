import requests, time

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from apps.qwerty_core.models import Text

class Command(BaseCommand):
    help = 'Searches for quotes from the Quotes API and saves useful ones in the database'

    def format_quote(self, quote):
        quote = quote.replace('”', '"').replace('“', '"')
        quote = quote.replace('’', "'").replace('‘', "'")
        quote = quote.replace('…', '...')
        quote = quote.replace("«", "").replace("»", "")
        quote = quote.replace('\r\n', ' ').replace('\n', ' ').replace('\r', ' ')
        return quote

    def handle(self, *args, **options):
        for lang in settings.ALLOWED_LANGUAGES.keys():
            self.stdout.write(self.style.SUCCESS(f'Seatching quotes for {lang}...'))
            total = 0
            while True:
                time.sleep(1)
                
                querystring = {
                    "language_code": lang
                }
                headers = {
                    "X-RapidAPI-Key": settings.QUOTES_API_KEY,
                    "X-RapidAPI-Host": settings.QUOTES_API_HOST
                }

                resp = requests.get(settings.QUOTES_API_URL, headers=headers, params=querystring)
                if resp.status_code != 200:
                    self.stdout.write(self.style.ERROR(f'Error searching quotes for {lang}'))
                    continue
                
                data = resp.json()
                quote = self.format_quote(data['content'])

                if len(quote) < 95 or len(quote) > 350: continue
                if Text.objects.filter(text=quote).exists(): continue

                print(f"Saving quote: {quote}")
                
                Text.objects.create(text=quote, lang=lang)
                total += 1
                print(f"Total saved: {total}")
                if total == 100: break