from django.shortcuts import render,redirect
from . models import comp_log,comp_det
from UserApp.models import Cart_tbl
# Create your views here.
def compreg(request):
    if request.method=='POST':
        cnm = request.POST.get('nm')
        eml = request.POST.get('em')
        psw = request.POST.get('ps')
        obj = comp_log.objects.create(cnm=cnm,usr=eml,psw=psw)
        obj.save()
        if obj:
            return render(request,"log.html")
        else:
            return render(request,"compreg.html")
    else:
        return render(request,"compreg.html")
    
def comphome(request):
    return render(request,"commoncomphome.html")

def proddetails(request):
    usr = request.session['usr']
    usr = str(usr)
    com = usr.split('@')[0]
    if request.method=='POST':
        cnm = request.POST.get('cnm')
        cat = request.POST.get('cat')
        cat = str(cat)
        cat = cat.lower()
        pro = request.POST.get('pro')
        pic = request.FILES.get('pic')
        prc = request.POST.get('prc')
        des =  request.POST.get('des')
        obj = comp_det.objects.create(cnm=cnm,cat=cat,pro=pro,pic=pic,prc=prc,des=des)
        obj.save()
        if obj:
          
            msg = "Details Entered Successfully.."
            return render(request,"proddetails.html",{"success":msg})
    else:
        return render(request,"proddetails.html",{"usr":com})

def cartdelete(request):
    number = request.GET.get('idn')
    obj = Cart_tbl.objects.filter(id=number)
    obj.delete()
    return redirect('/prod')