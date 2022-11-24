from django.shortcuts import render

# Create your views here.
def condition(request):
    d=context={'a':400}
    return render(request,'condition.html',d)