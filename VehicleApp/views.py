from django.shortcuts import render
from . models import Vehicle_tbl
# Create your views here.
def vehiclereg(request):
    if request.method=='POST':
        vnm = request.POST.get('vnm')
        vno = request.POST.get('vno')
        dnm = request.POST.get('dnm')
        dim = request.FILES.get('dim')
        lcn = request.FILES.get('lcn')
        lno = request.POST.get('lno')
        loc = request.POST.get('loc')
        mob = request.POST.get('mob')
        add = request.POST.get('add')
        obb = Vehicle_tbl.objects.create(vnm=vnm,vno=vno,dnm=dnm,dim=dim,lcn=lcn,lno=lno,loc=loc,mob=mob,add=add)
        obb.save()
        if obb:
            msg = "Details Added Successfully..."
            return render(request,"vehicle.html",{"veh":msg})
    return render(request,"vehicle.html")