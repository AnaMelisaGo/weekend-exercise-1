from django.shortcuts import render


def pedidos(request):
    """
    Docstring for pedidos
    to view the table of pedidos
    """

    template = 'pedidos.html'
    context = {
        'pedidos': 'active',
    }
    return render(request, template, context)


def titulo(request):
    """
    Docstring for titulo
    
    :to view titulo general
    """
    template = 'titulo.html'
    context = {
        'titulo': 'active',
    }
    return render(request, template, context)