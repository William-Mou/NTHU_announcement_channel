from django.core.management.base import BaseCommand, CommandError
from backend.models import News

class Command(BaseCommand):
    help = '!!Clean the specific table in DB!!'
    
    def add_arguments(self, parser):
        parser.add_argument('tables', nargs='+', type=str)

    def handle(self, *args, **options):
        for table in options['tables']:
            try:
                eval(table + ".objects.all().delete()")
                print(table + "has been clean!")
            except:
                raise('table not found.')
