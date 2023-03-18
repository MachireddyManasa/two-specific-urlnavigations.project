from django.shortcuts import render

# Create your views here.
def dhoni(request):
    return render(request,'dhoni.html')


def kohli(request):
    return render(request,'kohli.html')
