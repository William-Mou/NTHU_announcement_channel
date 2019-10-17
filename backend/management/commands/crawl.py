from django.core.management.base import BaseCommand, CommandError
from backend.crawler import schools, url_list
from backend.crawler import crawl


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    
    def add_arguments(self, parser):
        parser.add_argument('schools', nargs='+', type=str)

    def handle(self, *args, **options):
        """Crawl the specific school

        ** warning, 'eval' is not a secure method, we should find a way to
           avoid it !"""

        for sc in options['schools']:
            if sc.upper() in schools.schools:
                for dep in eval('schools.'+sc.upper()):
                    for office, link in eval('url_list.'+dep+'.items()'):
                        eval('crawl.'+ dep + "(office='" + office + "',ta_link='" + link + "')")
