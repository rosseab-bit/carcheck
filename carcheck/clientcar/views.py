from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def clientmap(request):
    context = {
            'client': 'client map'
            }
    return render(request, 'clientindex.html', context)



