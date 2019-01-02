from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def masterdataview(request):
    return HttpResponse("MasterData view!")
