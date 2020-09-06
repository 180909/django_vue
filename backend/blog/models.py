from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    content = models.CharField(max_length=1024, verbose_name="正文")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "blog"