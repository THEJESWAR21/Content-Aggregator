from articleFeed.models import Source, Authors, Articles
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Display RSS Aggreagtor Statistics"

    def handle(self, *args, **options):
        
        source_count = Source.objects.count()
        author_count = Authors.objects.count()
        articles_count = Articles.objects.count()

        self.stdout.write("=== RSS Aggregator Statistics ===")
        self.stdout.write(f"Source: {source_count}")
        self.stdout.write(f"Author: {author_count}")
        self.stdout.write(f"Articles: {articles_count}")
