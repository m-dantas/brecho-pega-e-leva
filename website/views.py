from django.shortcuts import render

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

    args = {
        'roupas': lista_roupas,
        'nome': nome,
        'idade': idade
    }
    return render(req, 'home.html', args)

def produtos(req):
    return render(req, 'produtos.html')