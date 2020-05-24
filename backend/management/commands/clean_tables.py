from django.core.management.base import BaseCommand, CommandError
import backend.models as models


class Command(BaseCommand):
    """Clean up table in the DB

    Usage: `python3 manage.py clean_tables News`
    """
    help = '!!Clean the specific table in DB!!'
    
    def add_arguments(self, parser):
        parser.add_argument('tables', nargs='+', type=str)

    def handle(self, *args, **options):
        for table in options['tables']:
            try:
                getattr(models, table).objects.all().delete()
                print(table + " has been clean!")
            except:
                raise('table not found.')
