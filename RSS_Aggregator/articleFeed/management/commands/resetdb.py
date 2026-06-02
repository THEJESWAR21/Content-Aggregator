from articleFeed.models import Source, Authors, Articles
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = "Resets and Delete All The Data in the Database"

    def handle(self, *args, **options):
        Articles.objects.all().delete()
        Authors.objects.all().delete()
        Source.objects.all().delete()

        self.stdout.write(
            self.style.SUCCESS("Database Cleared")
        )