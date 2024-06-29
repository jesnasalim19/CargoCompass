from django.shortcuts import render,redirect
from AdminApp.models import adminlog
from .models import reg_tbl,Cart_tbl,Pay_tbl,Trans_tbl,Auction,Bid_tbl
from ProApp.models import comp_det,comp_log
from DriverApp.models import Driver_tbl
from VehicleApp.models import Vehicle_tbl
from django.contrib import messages
from datetime import date,timedelta
# Create your views here.
def index(request):
    return render(request,"index.html")
def home(request):
    return render(request,"common.html")
def reg(request):
    if request.method=='POST':
        fnm = request.POST.get('nm')
        mob = request.POST.get('mb')
        eml = request.POST.get('em')
        psw = request.POST.get('ps')
        cpsw = request.POST.get('cps')
        obj = reg_tbl.objects.create(fnm=fnm,mob=mob,eml=eml,psw=psw,cpsw=cpsw)
        obj.save()
        if obj:
            return render(request,"log.html")
        else:
            return render(request,"reg.html")
    else:
        return render(request,"reg.html")
def log(request):
    if request.method=='POST':
        eml = request.POST.get('em')
        psw = request.POST.get('ps')
        obj = reg_tbl.objects.filter(eml=eml,psw=psw)
        obc = comp_log.objects.filter(usr=eml,psw=psw)
        obd = adminlog.objects.filter(eml=eml,psw=psw)
        if obj:
            for ls in obj:
                idno = ls.id
                request.session['idl']=idno
                obb = reg_tbl.objects.filter(id=idno)
            request.session['ema']=eml
            request.session['psa']=psw
            return render(request,"home.html",{"user":obb})
        elif obc:
            for m in obc:
                usr = m.usr
                request.session['usr']=usr
                com = usr.split('@')[0]
            return render(request,"comphome.html",{"user":com})
        elif obd:
            return render(request,"Admin_home.html")
        else:
            msg = "Invalid Email id & Password!.."
            return render(request,"log.html",{"error":msg})
    else:
        return render(request,"log.html")
def cat(request):
    return render(request,"category.html")
def prod(request):
    if request.method=='POST':
        sr = request.POST.get('sr')
        sr = str(sr)
        sr = sr.lower()
        obb = comp_det.objects.filter(cat=sr)
        return render(request,"products.html",{"pro":obb})
    return render(request,"category.html")
def addtocart(request):
    number = request.GET.get('idn')
    userid = request.session.get('idl')
    uobj = reg_tbl.objects.get(id=userid)
    pobj = comp_det.objects.get(id=number)
    cartitem,created = Cart_tbl.objects.get_or_create(customer=uobj,product=pobj)
    if not created:
        cartitem.qty+=1
        cartitem.save()
        messages.success(request,"Item added to cart")
    return redirect('/prod')
def viewcart(request):
    cid = request.session.get('idl')
    cusobj = reg_tbl.objects.get(id=cid)
    cartobj = Cart_tbl.objects.filter(customer=cusobj)
    if cartobj:
        total_price = 0
        for i in cartobj:
            pro=i.product.prc*i.qty
            total_price=total_price+pro
           
        return render(request,"cart.html",{'cartitems':cartobj,'total_price':int(total_price)})
    else:
        return render(request,"cart.html",{"info":"Your Cart is Empty"})
def paydirect(request):
    cid = request.session.get('idl')
    cusobj = reg_tbl.objects.get(id=cid)
    obb = reg_tbl.objects.filter(id=cid)
    for ls in obb:
        fnm = ls.fnm
    cartobj = Cart_tbl.objects.filter(customer=cusobj)
    if cartobj:
        total_price = 0
        for i in cartobj:
            pro=i.product.prc*i.qty
            total_price=total_price+pro
           
        return render(request,"pay.html",{'cartitems':cartobj,'total_price':int(total_price),"user":fnm})
    return render(request,"cart.html")
def pay(request):
    current_date = date.today()
    future_date = current_date + timedelta(days=9)
    idno =  request.session['idl']
    obj = reg_tbl.objects.filter(id=idno)
    for ls in obj:
        fname = ls.fnm
    vnm = Vehicle_tbl.objects.all()
    drv = Driver_tbl.objects.values_list('dnm', flat=True)
    vhc = Vehicle_tbl.objects.values_list('dnm', flat=True)
    alldrv = list(set(list(drv) + list(vhc)))  # Combine and remove duplicates
    if request.method=='POST':
        pro = request.POST.get('pro')
        qty = request.POST.get('qty')
        prc = request.POST.get('prc')
        tot = request.POST.get('tot')
        fn = request.POST.get('fn')
        cd = request.POST.get('cd')
        ex = request.POST.get('ex')
        cvv = request.POST.get('cvv')
        obb = Pay_tbl.objects.create(pro=pro,qty=qty,prc=prc,tot=tot,fn=fn,cd=cd,ex=ex,cvv=cvv)
        obb.save()
        if obb:
            msg = "Payment Successfull..."
            return render(request,"transport.html",{"success":msg,"ret":fname,"vnm":vnm,"alldrv":alldrv,"current_date": current_date,"future_date": future_date})
    return render(request,"pay.html")

def transport(request):
    if request.method=='POST':
        fnm = request.POST.get('fnm')
        vnm = request.POST.get('vnm')
        dnm = request.POST.get('dnm')
        address = request.POST.get('address')
        bd = request.POST.get('bd')
        dd = request.POST.get('dd')
        sc = request.POST.get('sc')
        obb = Trans_tbl.objects.create(fnm=fnm,address=address,bd=bd,dd=dd,sc=sc,vnm=vnm,dnm=dnm)
        obb.save()
        if obb:
            msg = "Your package will be delivered on the specified delivery date ..."
            return render(request,"success.html",{"success":msg})
    return render(request,"transport.html")

def Auction_details(request):
    idno =  request.session['idl']
    obj = reg_tbl.objects.filter(id=idno)
    for ls in obj:
        fname = ls.fnm
    if request.method=='POST':
        seller_name = request.POST.get('seller_name')
        item_name = request.POST.get('item_name')
        description = request.POST.get('description')
        good_img = request.FILES.get('good_img')
        basic_amount = request.POST.get('basic_amount')
        obj = Auction.objects.create(seller=seller_name,goods_name=item_name,goods_description=description, goods_image=good_img,basic=basic_amount)
        obj.save()
        if obj:
            msg = "Auction Details added Successfully.."
            return render(request,"Auction.html",{"success":msg})
    return render(request,"Auction.html",{"seller":fname})
def bid_submit(request):
    idno =  request.session['idl']
    obj = reg_tbl.objects.filter(id=idno)
    for ls in obj:
        fname = ls.fnm
    obj = Auction.objects.filter(ended=False)
    return render(request,"bid.html",{"data":obj,"bidder":fname})
def bid_max(request):
    if request.method=='POST':
        seller = request.POST.get('seller')
        gname = request.POST.get('gname')
        basic = request.POST.get('basic')
        st = request.POST.get('st')
        et = request.POST.get('et')
        bidder = request.POST.get('bidder')
        mb = request.POST.get('mb')
        obb = Bid_tbl.objects.create(seller=seller,gname=gname,basic=basic,st=st,et=et,bidder=bidder,mb=mb)
        obb.save()
        if obb:
            msg = "Your maximum bid amount entered..."
            return render(request,"bid.html",{"success":msg})
    return render(request,"bid.html")
def bid_result(request):
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
    return render(request,"bidresult.html",{"max":max_bid_price,"winner":winner_name,"good":goods_name,"st":st,"et":et,"seller":seller})
    




    



    
