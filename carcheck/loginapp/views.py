from django.shortcuts import render

# Create your views here.
def logindex(request):
    context={
            'url': 'login'
            }
    return render(request, 'logindex.html', context)
