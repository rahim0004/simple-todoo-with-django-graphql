import graphene
from graphene_django import DjangoObjectType
from .models import Todo
from django_filters import FilterSet

class TodoFilter(FilterSet):
    class Meta:
        model = Todo
        fields = ['title']

class TodoType(DjangoObjectType):

    id = graphene.ID(required=True)

    class Meta:
        model = Todo
        fields = ('id', 'title')
        filterset_class = TodoFilter
        interfaces = (graphene.relay.Node, )
        # connection_class = CountConnection

    def resolve_id(self, info, **kwargs):
        return self.id