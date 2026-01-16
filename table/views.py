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


def primer_base(request):
    """
    Docstring for primer_base
    
    :to view mi primer base
    """
    template = 'primer_base.html'
    context = {
        'base': 'active',
    }
    return render(request, template, context)


def fusion_columna(request):
    """
    Docstring for fusion_columna
    
    :to view fusion de columna
    """
    template = 'fusion_columna.html'
    context = {
        'fusion_columna': 'active',
    }
    return render(request, template, context)


def fusion_filas(request):
    """
    Docstring for fusion_filas
    
    :to view fusion de fila
    """
    template = 'fusion_filas.html'
    context = {
        'fusion_filas':'active',
    }
    return render(request, template, context)
