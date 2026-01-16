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