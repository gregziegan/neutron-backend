import graphene
from graphene import resolve_only_args, relay
from graphene.contrib.django import DjangoNode, DjangoConnectionField

from . import models

schema = graphene.Schema(name='Neutron Relay Schema')


class Connection(relay.Connection):
    total_count = graphene.IntField()

    def resolve_total_count(self, args, info):
        return len(self.get_connection_data())


class NewsOrganization(DjangoNode):
    class Meta:
        model = models.NewsOrganization
        exclude_fields = ('created', 'edited')


class Reference(DjangoNode):
    class Meta:
        model = models.Reference
        exclude_fields = ('created', 'edited')


class Article(DjangoNode):
    class Meta:
        model = models.Article
        exclude_fields = ('created', 'edited')


class User(DjangoNode):
    class Meta:
        model = models.User
        exclude_fields = ('created', 'edited')

    connection_type = Connection


class Query(graphene.ObjectType):
    all_news_organizations = DjangoConnectionField(NewsOrganization)
    all_references = DjangoConnectionField(Reference)
    all_articles = DjangoConnectionField(Article)
    all_users = DjangoConnectionField(User)
    news_organization = relay.NodeField(NewsOrganization)
    reference = relay.NodeField(Reference)
    article = relay.NodeField(Article)
    user = relay.NodeField(User)
    node = relay.NodeField()
    viewer = graphene.Field('self')

    @resolve_only_args
    def resolve_all_news_organizations(self, **kwargs):
        return models.NewsOrganization.objects.all()

    @resolve_only_args
    def resolve_all_references(self, **kwargs):
        return models.Reference.objects.all()

    @resolve_only_args
    def resolve_all_articles(self, **kwargs):
        return models.Article.objects.all()

    @resolve_only_args
    def resolve_all_users(self, **kwargs):
        return models.User.objects.all()

    def resolve_viewer(self, *args, **kwargs):
        return self


schema.query = Query

import json

introspection_dict = schema.introspect()

print(json.dumps(introspection_dict))
