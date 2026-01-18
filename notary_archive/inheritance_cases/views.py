from django.shortcuts import render

def index_ic(request):
    return render(request, 'inheritance_cases/index_ic.html')

def detail_ic(request):
    return render(request,'inheritance_cases/inheritance_card.html')
