from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls.base import reverse_lazy
from core.models import Cliente, Veiculo
from core.forms import FormCliente, FormVeiculo


def home(request):
    return render(request, "core/index.html")


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


@login_required
def cadastro_cliente(request):
    form = FormCliente(request.POST or None)
    contexto = {'form': form, 'acao':'Cadastro de Cliente', 'titulo':'Cadastar'}
    if form.is_valid():
        form.save()
        return redirect('url_listagem_clientes')
    else:        
        return render(request, "core/cadastro_cliente.html", contexto)


@login_required
def listagem_clientes(request):
    clientes = Cliente.objects.all()
    contexto = {'clientes': clientes}
    return render(request, "core/listagem_clientes.html", contexto)


@login_required
def cadastro_veiculo(request):
    form = FormVeiculo(request.POST or None, request.FILES or None)
    contexto = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('url_listagem_veiculos')
    else:
        return render(request, "core/cadastro_veiculo.html", contexto)


@login_required
def listagem_veiculos(request):
    veiculos = Veiculo.objects.all()
    contexto = {'veiculos': veiculos}
    return render(request, "core/listagem_veiculos.html", contexto)


@login_required
def atualiza_cliente(request, id):
    obj = Cliente.objects.get(id=id) 
    form = FormCliente(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form, 'acao':'Atualiza', 'titulo':'Atualiza'}
    if form.is_valid():
        form.save()
        return redirect('url_listagem_clientes')
    else:
        return render(request, "core/cadastro_cliente.html", contexto)


@login_required
def exclui_cliente(request, id):
    obj = Cliente.objects.get(id=id)
    if request.POST:
        obj.delete()
        return redirect('url_listagem_clientes')
    return render(request, 'core/comfirma_exclusao.html')