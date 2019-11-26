from django.shortcuts import render
from website.forms import PedidoForm
from website.models import Produto
# Create your views here.
def home(req):
    nome = 'Groger'
    idade = 17
    lista_roupas = [
        'Boné da Lacoste',
        'Boné da Cyclone',
        'Cinto do Bátima',
        'Toca da Medusa',
        'Óculos Rift Zika'
    ]

    context = {
        'roupas': lista_roupas,
        'nome': nome,
        'idade': idade
    }
    return render(req, 'home.html', context)

def produtos(req):
    produtos = Produto.objects.filter(disponivel=True)

    context = {
        'produtos': produtos
    }
    return render(req, 'produtos.html', context)

def cadastro_pedido(req):
    form = PedidoForm(req.POST or None)

    if form.is_valid():
        form.save()
        context = {
            'msg': 'Pedido realizado com sucesso'
        }
        return render(req, 'pedido.html', context)
    context = {
        'form': form
    }
    return render(req, 'pedido.html', context)