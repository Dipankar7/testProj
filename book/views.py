from django.shortcuts import render,redirect
from .models import Registration
from .forms import RegistrationForm

# Create your views here.

def Registration_User(request):
    if request.method == "POST":
        print "post method"
        form=RegistrationForm(request.POST)
        if form.is_valid():
            print "form is valid"
            chekinDate=request.POST.get('checkIn')
            form.save()
            print "form saved"
            print chekinDate
            context={'date1':chekinDate}
            request.session['_context']=context
            print "came here"
            return redirect('Thanks_User')
        else:
            print "Form is invalid"
    else:
        print "rendering blank form"
        form=RegistrationForm()
    return render(request,'book/registration.html',{'form':form})

def Thanks_User(request):
    context=request.session.get('_context')
    print context
    return render(request,'book/thanks.html',context)