from articleFeed.models import Source, Authors, Articles
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        Articles.objects.all().delete()
        Authors.objects.all().delete()
        Source.objects.all().delete()

        self.stdout.write(
            self.style.SUCCESS("Database Cleared")
        )