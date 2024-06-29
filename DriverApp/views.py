from django.shortcuts import render
from . models import Driver_tbl
# Create your views here.
def driverreg(request):
    if request.method=='POST':
        dnm = request.POST.get('dnm')
        dim = request.FILES.get('dim')
        lno = request.POST.get('lno')
        lcn = request.FILES.get('lcn')
        loc = request.POST.get('loc')
        mob = request.POST.get('mob')
        add = request.POST.get('add')
        obb = Driver_tbl.objects.create(dnm=dnm,dim=dim,lno=lno,lcn=lcn,loc=loc,mob=mob,add=add)
        obb.save()
        if obb:
            msg = "Details Added Successfully..."
            return render(request,"driver.html",{"veh":msg})
    return render(request,"driver.html")