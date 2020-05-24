from django.core.management.base import BaseCommand, CommandError
from backend.crawler import crawl
from django.conf import settings
import json


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    
    def add_arguments(self, parser):
        parser.add_argument('schools', nargs='+', type=str)

    def handle(self, *args, **options):
        """Crawl the specific school
        """
        with open(f"{settings.BASE_DIR}/backend/crawler/url_list.json", 'r') as f:
            schools = json.loads(f.read())

        for sc in options['schools']:
            school = sc.upper()
            if school not in schools:
                print(f"The school does not exist: {school}")
                continue

            for dep, detail in schools[school]['dep'].items():
                for office, link in detail['url'].items():
                    getattr(crawl, school + '_' + dep)(office=office, ta_link=link)
