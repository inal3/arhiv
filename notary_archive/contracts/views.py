from django.shortcuts import render

def index_contracts(request):
    return render(request, 'contracts/index_contracts.html')
