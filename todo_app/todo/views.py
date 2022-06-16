from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import ToDo
from .forms import ToDoForm

def index(request):
    todo_list = ToDo.objects.order_by('id')

    form = ToDoForm()

    context = {'todo_list' : todo_list, 'form' : form}
    return render(request, 'todo/index.html', context)


@require_POST
def add_to_do(request):
    form = ToDoForm(request.POST)

    if form.is_valid():
        new_todo = ToDo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')


def complete_to_do(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    if todo.complete:
        todo.complete = False
    else:
        todo.complete = True

    todo.save()

    return redirect('index')


def delete_completed(request):
    ToDo.objects.filter(complete__exact=True).delete()

    return redirect('index')


def delete_all(request):
    ToDo.objects.all().delete()

    return redirect('index')


