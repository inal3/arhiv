from django.shortcuts import render

def index_ic(request):
    return render(request, 'inheritance_cases/index_ic.html')
