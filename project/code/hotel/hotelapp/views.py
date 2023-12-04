from django.shortcuts import render
from hotelapp.models import booking_modelTable,addroom_modelTable,customer_modelTable
from hotelapp.forms import addroom_RegForm,customer_RegForm

# Create your views here.
def home(request):
    return render(request,'home.html')
def adminlog(request):
    return render(request,'adminlogin.html')    
def adminlogin(request):
    N=request.POST['name']
    P=request.POST['pw']
    print(N,P)
    if(N=='admin' and P=='1234'):
        return render(request,'adminhome.html')
    else:
        return render(request,'adminlogin.html')
def cuslog(request):
    return render(request,'customerlogin.html')    
def customerhome(request):
    return render(request,'customerhome.html')    
def customerlogin(request):
    N=request.POST['name']
    P=request.POST['pw']
    a=customer_modelTable.objects.all().filter(name=N,mbl=P).values()
    if not a:
        return render(request,'customerlogin.html')
    else:
        id=a[0]['id']
        request.session['name']=N
        request.session['id']=id
        return render(request,'customerhome.html',{'name':N,'id':id})   
def adminhome(request):
    return render(request,'adminhome.html')    
def adminlink(request):
    return render(request,'adminhome.html')  
def cusreg(request):
    reg=customer_RegForm(request.POST)
    if(reg.is_valid()):
        reg.save()
        return render(request,"customerregistration.html",{'myform':reg}) 
    else:
        return render(request,"customerregistration.html",{'myform':reg}) 
def room(request):
    return render(request,'addroom.html')        
def addroom(request):
    reg=addroom_RegForm(request.POST)   
    if(reg.is_valid()):
        reg.save()  
        return render(request,"addroom.html",{'myform':reg}) 
    else:
        return render(request,"addroom.html",{'myform':reg})    
def customerviewroom(request):
    a=addroom_modelTable.objects.all().filter(status='available')
    print(a)
    if not a:
        return render(request,'customerhome.html')
    else:
        return render(request,'customerviewroom.html',{'data':a})   
def roomcheckin(request):
    rid=request.GET['roomid']
    #n=request.session['name']
    uid=request.session['id']
    st='checkin'
    st2='not available'
    st3=booking_modelTable()
    st3.rid=rid
    st3.uid=uid
    st3.status=st
    st3.save()
    addroom_modelTable.objects.all().filter(id=rid).update(status=st2)
    a=addroom_modelTable.objects.all().filter(status='available')
    print(a)
    if not a:
        return render(request,'customerhome.html')
    else:
        return render(request,'customerviewroom.html',{'data':a})
def checkout(request):
    uid=request.session['id']
    print(uid)
    d=booking_modelTable.objects.all().filter(uid=uid,status='checkin').values()   
    if not d:
        return render(request,'customerhome.html',{'data':d})
    else:
       return render(request,'customercheckout.html',{'data':d})  
def checkout1(request):
    rid=int(request.GET['roomid'])
    bid=int(request.GET['bookid'] )
    st1='available'
    st2='checkout'
    print(bid)
    booking_modelTable.objects.all().filter(bid=bid).update(status=st2)
    addroom_modelTable.objects.all().filter(id=rid).update(status=st1)
    return render(request,'customerhome.html')
def adminviewcheckin(request):

    d=booking_modelTable.objects.all().filter(status='checkin')
    if not d:
        return render(request,'adminhome.html')
    else:
       return render(request,'adminviewcheckin.html',{'data':d}) 
def adminviewcheckout(request):
    d=booking_modelTable.objects.all().filter(status='checkout')
    if not d:
        return render(request,'adminhome.html')
    else:
       return render(request,'adminviewcheckout.html',{'data':d}) 

def adminviewcustomer(request):
    d=customer_modelTable.objects.all()
    if not d:
        return render(request,'adminhome.html')
    else:
        return render(request,'adminviewcustomer.html',{'data':d})    







        


