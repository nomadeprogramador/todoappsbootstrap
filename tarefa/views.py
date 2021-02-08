from django.shortcuts import render,redirect
from .models import Tarefa
# Create your views here.
def index (request):
    tarefa=Tarefa.objects.all()
    if request.POST:
        tarefa=request.POST.get('tarefa')
        tarefa=Tarefa(conteudo=tarefa)
        tarefa.save()
        return redirect('/')
    context={
        'tarefa':tarefa,
    }
    return render(request,'tarefas/index.html',context)
def excluir_tarefa(request,id):
    tarefa=Tarefa.objects.get(id=id)
    tarefa.delete()
    return redirect('/')