from django.shortcuts import render


def home(request):
    return render(request, "core/index.html")


def cadastro_cliente(request):
    return render(request, "core/cadastro_cliente.html")


def listagem_clientes(request):
    return render(request, "core/listagem_clientes.html")


def cadastro_veiculo(request):
    return render(request, "core/cadastro_veiculo.html")


def listagem_veiculos(request):
    return render(request, "core/listagem_veiculos.html")
