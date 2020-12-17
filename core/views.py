from django.forms.forms import Form
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls.base import reverse_lazy
from core.models import Cliente, Veiculo, Parametro, Movimento, Mensalista
from core.forms import FormCliente, FormVeiculo,\
    FormParametro, FormMovimento, FormMensalista


def home(request):
    return render(request, "core/index.html")


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


@login_required
def cadastro_cliente(request):
    form = FormCliente(request.POST or None)
    contexto = {'form': form, 'acao': 'Cadastro de Cliente', 'titulo': 'Cadastar'}
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
    contexto = {'form': form, 'acao': 'Atualiza', 'titulo': 'Atualiza'}
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


@login_required
def cadastro_parametro(request):
    form = FormParametro(request.POST or None)
    contexto = {'form': form, "acao": 'Cadastro De Pâmetro'}
    if form.is_valid():
        form.save()
        return redirect('url_listagem_parametros')
    else:
        return render(request, "core/cadastro_parametro.html", contexto)


@login_required
def listagem_parametros(request):
    dados = Parametro.objects.all()
    contexto = {'parametros': dados}
    return render(request, 'core/listagem_parametros.html', contexto)


@login_required()
def cadastro_mensalista(request):
    form = FormMensalista(request.POST or None)
    contexto = {'form': form, 'acao': 'Cadastro de Mensalista'}
    if form.is_valid():
        form.save()
        return redirect('url_listagem_mensalistas')
    else:
        return render(request, 'core/cadastro_mensalista.html', contexto)


@login_required()
def listagem_mensalistas(request):
    dados = Parametro.objects.all()
    contexto = {'mensalistas': dados}
    return render(request, 'core/listagem_mensalistas.html', contexto)


@login_required()
def atualiza_parametro(request, id):
    try:
        obj = Parametro.objects.get(id=id)
        form = FormParametro(request.POST or None, instance=obj)
        contexto = {'form': form, 'acao': 'Atualização de Parâmetro'}
        if form.is_valid():
            form.save()
            return redirect('url_listagem_parametros')
        else:
            return render(request, 'core/cadastro_parametro.html', contexto)
    except Exception as erro:
        return redirect('url_listagem_parametros')


@login_required()
def exclui_parametro(request, id):
    try:
        obj = Parametro.objects.get(id=id)
        contexto = {'acao': obj.descricao, 'redirect': '/listagem_parametros/'}
        if request.method == 'POST':
            obj.delete()
            return redirect('url_listagem_parametros')
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)
    except Exception as erro:
        return redirect('url_listagem_parametros')


@login_required()
def cadastro_movimento(request):
    if request.user.is_staff:
        form = FormMovimento(request.POST or None)
        contexto = {'form': form, 'titulo': 'Cad:Movimento', 'acao': 'Cadastro de Movimento'}
        if form.is_valid():
            form.save()
            return redirect('url_listagem_movimento')

        return render(request, "core/cadastro_movimento.html", contexto)
    else:
        contexto = {'erro': 'Voçe não tem permição procure o gerente'}
        return render(request, 'core/erro.html', contexto)


@login_required
def listagem_movimento(request):
    dados = Movimento.objects.all()
    contexto = {'movimento': dados}
    return render(request, "core/listagem_movimento.html", contexto)


@login_required
def atualiza_movimento(request, id):
    if request.user.is_staff:
        obj = Movimento.objects.get(id=id)
        form = FormMovimento(request.POST or None, instance=obj)
        contexto = {'form': form, 'acao': 'Atualiza Movimento', 'titulo': 'AtuMov:G4car'}
        if form.is_valid():

            form.save()
            return redirect('url_listagem_movimento')
        else:
            return render(request, 'core/cadastro_movimento.html', contexto)

    else:
        contexto = {'erro' : 'Voçe não tem permição procure o gerente'}
        return render(request, 'core/erro.html', contexto)