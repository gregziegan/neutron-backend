from django.db import models
from django.contrib.auth.models import User

class DateTimeModel(models.Model):
    """ A base model with created and edited datetime fields """

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NewsOrganization(DateTimeModel):
    name = models.CharField(max_length=100)
    url = models.URLField()
    bias = models.PositiveSmallIntegerField()


class Reference(DateTimeModel):
    """ Content referenced by news articles """
    reputability = models.PositiveSmallIntegerField()
    url = models.URLField(max_length=400)


class Article(DateTimeModel):
    """ An article published by a News Organization """
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.URLField(max_length=400)
    news_organization = models.ForeignKey(NewsOrganization)
    references = models.ManyToManyField(
        Reference,
        "citations",
        blank=True
    )
