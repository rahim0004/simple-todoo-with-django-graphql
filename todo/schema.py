import graphene
from .forms import TodoForm
from .models import Todo
from .objectTypes import TodoType
from graphene_django.forms.types import DjangoFormInputObjectType
from graphene_django.filter import DjangoFilterConnectionField


class TodoInput(DjangoFormInputObjectType):
    class Meta:
        form_class = TodoForm

class TodoMutation(graphene.Mutation):
    todo =  graphene.Field(TodoType)

    class Arguments:
        todo_data = TodoInput(required=True)
    
    def mutate(self, info, todo_data):
        todo = Todo.objects.create(**todo_data)
        return TodoMutation(todo=todo)
    

class Mutation(graphene.ObjectType):
    create_todo = TodoMutation.Field()



class Query(graphene.ObjectType):
    todos = DjangoFilterConnectionField(TodoType)
    todo = graphene.Field(TodoType, id=graphene.ID(required=True))


    def resolve_todos(self, info, **kwargs):
        return Todo.objects.all()
    
    def resolve_todo(self, info, id):
        return Todo.objects.get(id=id)
    



schema = graphene.Schema(query=Query, mutation=Mutation)