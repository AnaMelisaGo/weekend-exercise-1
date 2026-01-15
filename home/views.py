from django.shortcuts import render

# Create your views here.
def index(request):
    """
    To view index
    """
    template = 'home/index.html'
    context = {}
    return render(request, template, context)