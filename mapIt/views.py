from django.shortcuts import render,redirect
from django.db import connection
import json

from .forms import detailsForm
# Create your views here.

def mainPage(request):
    if request.method=="POST":
        form=detailsForm(request.POST)
        if form.is_valid():
            phoneNumber=request.POST.get('phoneNumber')
            cursor = connection.cursor()
            phoneNumber_arr=phoneNumber.split(",")
            print phoneNumber_arr
            for i in range(len(phoneNumber_arr)):
                if phoneNumber_arr[i][0]=="+":
                    temp=phoneNumber_arr[i]
                    phoneNumber_arr[i]=temp[3:]
            print phoneNumber_arr
            locations={}
            context={}
            not_found=[]

            for i in phoneNumber_arr:
                if(cursor.execute("select latitude,longitude,name from easy_maps_address_temp where phoneNumber=%s",[i])):
                    data=cursor.fetchone()
                    print data,i
                    print "printing json",json.dumps(data)
                    loc=[]
                    loc.append(data[0])
                    loc.append(data[1])
                    print loc,"From for loop",i
                    locations[data[2]]=loc
                else:
                    not_found.append(i)
            context['locations']=locations
            context['not_found']=not_found
            print "sending context to info",context
            request.session['_context']=context
            return redirect('info_page')
        else:
            print "error in form"
    else:
        form=detailsForm()

    return render(request,'mainPage.html',{'form':form})


def infoPage(request):
    context=request.session['_context']
    myCenter=[]
    if context['locations']:
        myCenter=context['locations'].itervalues().next()
    context['myCenter']=myCenter
    print "in info page"
    print context
    print json.dumps(context['locations'])
    return render(request,'infoPage.html',context)
