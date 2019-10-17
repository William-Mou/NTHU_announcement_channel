from django.db import models


class NewsManager(models.Manager):
    @staticmethod
    def add(school, dep, title, category, url):
        """Add the record to the DB"""

        "Check if the new exist in the DB"
        if News.objects.filter(dep=dep, url=url).exists():
            return False
        else:
            News.objects.create(school=school, dep=dep, category=category, title=title, url=url)


class News(models.Model):
    school = models.CharField(max_length=50, verbose_name='學校')
    dep = models.CharField(max_length=30, blank=True, null=True, verbose_name='系所')
    title = models.CharField(max_length=200, verbose_name="標題")
    category = models.CharField(max_length=50)
    url = models.URLField(max_length=200, verbose_name="網址")
    published = models.BooleanField(default=False, verbose_name="是否寄送過")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='建立時間')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='建立時間')

    objects = NewsManager()

