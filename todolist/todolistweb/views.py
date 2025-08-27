from django.shortcuts import render,redirect,get_object_or_404
from .models import Task,Notas # importamos models para ocupar la base de datos como objeto
# Create your views here.

def home(request):
    return render(request,'home.html')

def task_list(request):
    tasks = Task.objects.all() #consulta todos los objetos de la base de datos Task creada en models
    return render(request,"tasks/task_list.html",{"tasks":tasks}) 

def task_add(request):
    if request.method =="POST": # 1. Si el usuario envía el formulario
        title = request.POST.get("title") # 2. Obtenemos el valor del input
        if title:
            Task.objects.create(title=title) # 3. Creamos tarea en BD
        
        return redirect("task_list") # nos devuelve a la pagina de lista de tareas
    return render(request,"tasks/task_add.html")

def task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id) # 1. Buscar la tarea o dar error 404
    task.completed = True   # 2. Cambiar estado
    task.save()             # 3. Guardar en BD
    return redirect("task_list")  # 4. Redirigir


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("task_list")


##notas

def nota_list(request):
    notas = Notas.objects.all() #aqui le pasamos el objeto de notas
    return render(request,"notas/notas_list.html", {"notas":notas})

def notas_add(request):
    if request.method=="POST":
        title = request.POST.get("title")
        if title:
            Notas.objects.create(title=title)
        
        return redirect("notas_list")
    return render(request,"notas/notas_add.html")

def notas_delete(request, nota_id):
    notas= get_object_or_404(Notas, id=nota_id)
    notas.delete()
    return redirect("notas_list")


    