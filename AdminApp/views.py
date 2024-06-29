from django.shortcuts import render,redirect
from UserApp.models import reg_tbl,Auction,Bid_tbl
from DriverApp.models import Driver_tbl
from VehicleApp.models import Vehicle_tbl
# Create your views here.

def Adminhome(request):
    return render(request,"Admin_home.html")

def userview(request):
    obj = reg_tbl.objects.all()
    return render(request,"user_details.html",{"data":obj})

def edit(request):
    idno = request.GET.get('idn')
    obj = reg_tbl.objects.filter(id=idno)
    return render(request,"edit.html",{"data":obj})

def update(request):
    if request.method=='POST':
        fnm = request.POST.get('fn')
        idno = request.POST.get('idl')
        mob = request.POST.get('mb')
        eml = request.POST.get('em')
        psw = request.POST.get('ps')
        reg_tbl.objects.filter(id=idno).update(fnm=fnm,mob=mob,eml=eml,psw=psw)
        return redirect("/AdminApp/userview")
    return render(request,"edit.html")
        

def delete(request):
    idno = request.GET.get('idn')
    obj = reg_tbl.objects.filter(id=idno)
    obj.delete()
    return redirect("/AdminApp/userview")

def driverview(request):
    obj = Driver_tbl.objects.all()
    return render(request,"driver_view.html",{"data":obj})

def driveredit(request):
    idno = request.GET.get('idn')
    obj = Driver_tbl.objects.filter(id=idno)
    return render(request,"driveredit.html",{"data":obj})

def driverupdate(request):
    if request.method=='POST':
        dnm = request.POST.get('dn')
        idno = request.POST.get('idl')
        dim = request.FILES.get('di')
        lno = request.POST.get('ln')
        lcn = request.FILES.get('lc')
        loc = request.POST.get('lo')
        mob = request.POST.get('mo')
        add = request.POST.get('ad')
        Driver_tbl.objects.filter(id=idno).update(dnm=dnm,dim=dim,lno=lno,lcn=lcn,loc=loc,mob=mob,add=add)
        return redirect("/AdminApp/driverview")
    return render(request,"driveredit.html")

def driverdelete(request):
    idno = request.GET.get('idn')
    obj = Driver_tbl.objects.filter(id=idno)
    obj.delete()
    return redirect("/AdminApp/driverview")

def vehicleview(request):
    obj = Vehicle_tbl.objects.all()
    return render(request,"vehicle_view.html",{"data":obj})

def vehicleedit(request):
    idno = request.GET.get('idn')
    obj = Vehicle_tbl.objects.filter(id=idno)
    return render(request,"vehicleedit.html",{"data":obj})

def vehicleupdate(request):
    if request.method=='POST':
        vnm = request.POST.get('vnm')
        vno = request.POST.get('vno')
        dnm = request.POST.get('dn')
        idno = request.POST.get('idl')
        dim = request.FILES.get('di')
        lno = request.POST.get('ln')
        lcn = request.FILES.get('lc')
        loc = request.POST.get('lo')
        mob = request.POST.get('mo')
        add = request.POST.get('ad')
        Vehicle_tbl.objects.filter(id=idno).update(vnm=vnm,vno=vno,dnm=dnm,dim=dim,lno=lno,lcn=lcn,loc=loc,mob=mob,add=add)
        return redirect("/AdminApp/vehicleview")
    return render(request,"vehicleedit.html")

def vehicledelete(request):
    idno = request.GET.get('idn')
    obj = Vehicle_tbl.objects.filter(id=idno)
    obj.delete()
    return redirect("/AdminApp/vehicleview")


def Auction_view(request):
    obj = Auction.objects.all()
    return render(request,"Auction_view.html",{"data":obj})


def auction_end(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('ended_'):
                auction_id = key.split('_')[1]
                ended = value == 'on'  # Convert 'on' to True
                Auction.objects.filter(id=auction_id).update(ended=ended)
        return redirect("/AdminApp/Auction_view")
    return render(request, "Auction_view.html")

def adminbid_view(request):
    obj = Bid_tbl.objects.all()
    return render(request,"Admin_bidview.html",{"data":obj})

def adminbid_result(request):
    obb = Bid_tbl.objects.all()
    max_bid_price = 0
    winner_name = ""
    # Iterate through all bids to find the maximum bid price and the corresponding bidder
    for bid in obb:
        bid.mb = int(bid.mb)
        if bid.mb > max_bid_price:
            max_bid_price = bid.mb
            winner_name = bid.bidder
            goods_name = bid.gname
            seller = bid.seller
            st = bid.st
            et = bid.et

    # Now 'winner_name' contains the name of the bidder with the maximum bid price
    return render(request,"adminbidresult.html",{"max":max_bid_price,"winner":winner_name,"good":goods_name,"st":st,"et":et,"seller":seller})
    

