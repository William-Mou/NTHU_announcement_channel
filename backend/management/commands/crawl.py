from django.core.management.base import BaseCommand, CommandError
from backend.crawler import NTHU_CS

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    
    def add_arguments(self, parser):
        parser.add_argument('deps', nargs='+', type=str)

    def handle(self, *args, **options):
        for dep in options['deps']:
            NTHU_CS.do()
