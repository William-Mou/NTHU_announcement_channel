from django.core.management.base import BaseCommand, CommandError
from backend.models import News
from backend.MSG import line, tg
from time import sleep


class Command(BaseCommand):
    help = 'Send message which is not published.'

    def handle(self, *args, **options):
        """ Not complete!!! """
        news_list = News.objects.get_not_published()
        for news in news_list:
            tg.send_msg(news.category, news.title, news.url)
            # line.send_msg(news.dep, news.title, news.url)
            # 將該筆資料改成已傳送
            news.published = True
            news.save()
            # 避免太頻繁發送被 ban
            sleep(5)
