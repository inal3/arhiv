from django.shortcuts import render

def index_testaments(request):
    return render(request, 'testaments/index_testaments.html')
