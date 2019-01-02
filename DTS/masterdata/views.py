from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def masterdataview(request):
# this is the old response. The new version uses the template
# return HttpResponse("MasterData view!")
    masterdata_dict = {
        'bodymasterdata':"Hello the message is now coming from view.py for masterdata"
    }
    return render(request,'masterdata/index.html',context=masterdata_dict)
