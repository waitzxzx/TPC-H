from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt

from DBHW import models
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger





def Nation_list(request):
    nation_list = models.Nation.objects.all()
    paginator = Paginator(nation_list, 10)
    page = request.GET.get('page', 1)
    try:
        nation = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        nation = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        nation = paginator.page(paginator.num_pages)
    return render(request, 'nationlist.html', {"nation_list":nation})

@csrf_exempt
def Nation_Edit(request,nid):
    if request.method == "POST":
        nationkey = request.POST.get('n_nationkey')
        name = request.POST.get('n_name')
        regionkey = request.POST.get('n_regionkey')
        comment = request.POST.get('n_comment')
        models.Nation.objects.filter(n_nationkey=nid).update(n_nationkey=nationkey,n_name = name,n_regionkey =regionkey,n_comment =comment)
        return HttpResponseRedirect("/DBHW/nationlist/")
    else:
        obj = models.Nation.objects.filter(n_nationkey=nid).first()
        region_list =models.Region.objects.all().values_list('r_regionkey','r_name')
        #一般返回objects .values_list返回字典 .value返回元组#
        print(region_list)
        return render(request, 'nationedit.html', {"obj":obj,"region_list":region_list})


def Nation_delete(request,nid):
        models.Nation.objects.filter(n_nationkey=nid).delete()
        return render(request, 'nationdelete.html')

@csrf_exempt
def Nation_view(request, nid):
        obj = models.Nation.objects.filter(n_nationkey=nid).first()
        return render(request, 'nationview.html', {"obj": obj})


@csrf_exempt
def Nation_add(request):
    if request.method == "POST":
        nationkey = request.POST.get('n_nationkey')
        name = request.POST.get('n_name')
        regionkey = request.POST.get('n_regionkey')
        comment = request.POST.get('n_comment')
        region = models.Region.objects.get(r_regionkey=regionkey)
        obj = models.Nation(n_nationkey=nationkey,n_name = name,n_regionkey =region,n_comment =comment)
        obj.save()
        return HttpResponseRedirect("/DBHW/nationlist/")
    else:
        region_list = models.Region.objects.all().values_list('r_regionkey', 'r_name')
        # 一般返回objects .values返回字典 .value_list返回元组#
        print(region_list)
        return render(request, 'nationadd.html',{"region_list":region_list})


def Customer_list(request):
    customer_list = models.Customer.objects.all()
    paginator = Paginator(customer_list, 10)
    page = request.GET.get('page', 1)
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        customer = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        customer = paginator.page(paginator.num_pages)
    return render(request, 'customerlist.html', {"customer_list":customer})


@csrf_exempt
def Customer_Edit(request,nid1,nid2):
    if request.method == "POST":
        custkey = request.POST.get('c_custkey')
        name = request.POST.get('c_name')
        address = request.POST.get('c_address')
        nationkey = request.POST.get('c_nationkey')
        phone = request.POST.get('c_phone')
        accbal = request.POST.get('c_acctbal')
        mktsegment = request.POST.get('c_mktsegment')
        comment = request.POST.get('c_comment')
        models.Customer.objects.filter(c_custkey=nid2).update(c_custkey=custkey,c_name = name,c_address =address,c_nationkey =nationkey,
                                                           c_phone=phone,c_acctbal=accbal,c_mktsegment=mktsegment,c_comment=comment)
        return HttpResponseRedirect("/DBHW/customerlist/")
    else:
        obj = models.Customer.objects.filter(c_custkey=nid2).first()
        return render(request, 'customeredit.html', {"obj":obj})

def Customer_delete(request, nid):
    models.Customer.objects.filter(c_custkey=nid).delete()
    return render(request, 'customerdelete.html')


@csrf_exempt
def Customer_view(request, nid):
    obj = models.Customer.objects.filter(c_custkey=nid).first()
    return render(request, 'customerview.html', {"obj": obj})


@csrf_exempt
def Customer_add(request):
    if request.method == "POST":
        custkey = request.POST.get('c_custkey')
        name = request.POST.get('c_name')
        address = request.POST.get('c_address')
        nationkey = request.POST.get('c_nationkey')
        phone = request.POST.get('c_phone')
        accbal = request.POST.get('c_acctbal')
        mktsegment = request.POST.get('c_mktsegment')
        comment = request.POST.get('c_comment')
        nation = models.Nation.objects.get(n_nationkey=nationkey)
        obj = models.Customer(c_custkey=custkey,c_name = name,c_address =address,c_nationkey =nation,
                              c_phone=phone,c_acctbal=accbal,c_mktsegment=mktsegment,c_comment=comment)
        obj.save()
        return HttpResponseRedirect("/DBHW/customerlist/")
    else:
        return render(request, 'customeradd.html')

def Lineitem_list(request):
    lineitem_list = models.Lineitem.objects.all()
    paginator = Paginator(lineitem_list, 10)
    page = request.GET.get('page', 1)
    try:
        lineitem = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        lineitem = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        lineitem = paginator.page(paginator.num_pages)
    return render(request, 'lineitemlist.html', {"lineitem_list":lineitem})

@csrf_exempt
def Lineitem_Edit(request,nid,uid):
    if request.method == "POST":
        orderkey = request.POST.get('l_orderkey')
        partkey = request.POST.get('l_partkey')
        suppkey = request.POST.get('l_suppkey')
        linenumber = request.POST.get('l_linenumber')
        quantity = request.POST.get('l_quantity')
        if quantity == '':
            quantity = 0
        extendedprice = request.POST.get('l_extendedprice')
        if extendedprice == '':
            extendedprice = 0
        discount = request.POST.get('l_discount')
        if discount == '':
            discount = 0
        tax = request.POST.get('l_tax')
        if tax == '':
            tax = 0
        returnflag = request.POST.get('l_returnflag')
        linestatus = request.POST.get('l_linestatus')
        shipdate = request.POST.get('l_shipdate')
        commitdate = request.POST.get('l_commitdate')
        receiptdate = request.POST.get('l_receiptdate')
        shipinstruct = request.POST.get('l_shipinstruct')
        shipmode = request.POST.get('l_shipmode')
        comment = request.POST.get('l_comment')
        obj1 = models.Orders.objects.get(o_orderkey=nid)
        obj2 = models.Lineitem.objects.get(l_linenumber=uid)
        tem = float(extendedprice) - obj2.l_extendedprice
        sum = obj1.o_totalprice + tem
        models.Orders.objects.filter(o_orderkey=nid).update(o_totalprice = sum)
        models.Lineitem.objects.filter(l_linenumber=uid).update(l_orderkey=orderkey,l_partkey = partkey,l_suppkey =suppkey,
                                                            l_linenumber =linenumber,l_quantity=quantity,l_extendedprice=extendedprice,
                                                            l_discount=discount,l_tax=tax,l_returnflag=returnflag,l_linestatus=linestatus,
                                                            l_shipdate=shipdate,l_commitdate=commitdate,l_receiptdate=receiptdate,l_shipinstruct=shipinstruct,
                                                            l_shipmode=shipmode,l_comment=comment)
        return HttpResponseRedirect("/DBHW/lineitemlist/")
    else:
        obj = models.Lineitem.objects.filter(l_orderkey=nid).first()
        return render(request, 'lineitemedit.html', {"obj":obj})

def Lineitem_delete(request, nid,uid):
    models.Lineitem.objects.filter(l_orderkey=nid).delete()
    return render(request, 'lineitemdelete.html')


@csrf_exempt
def Lineitem_view(request, nid):
    obj = models.Lineitem.objects.filter(l_orderkey=nid).first()
    return render(request, 'lineitemview.html', {"obj": obj})

@csrf_exempt
def Lineitem_Add(request):
    if request.method == "POST":
        orderkey = request.POST.get('l_orderkey')
        partkey = request.POST.get('l_partkey')
        suppkey = request.POST.get('l_suppkey')
        linenumber = request.POST.get('l_linenumber')
        quantity = request.POST.get('l_quantity')
        if quantity == '':
            quantity = 0
        extendedprice = request.POST.get('l_extendedprice')
        if extendedprice == '':
            extendedprice = 0
        discount = request.POST.get('l_discount')
        if discount == '':
            discount = 0
        tax = request.POST.get('l_tax')
        if tax == '':
            tax = 0
        returnflag = request.POST.get('l_returnflag')
        linestatus = request.POST.get('l_linestatus')
        shipdate = request.POST.get('l_shipdate')
        commitdate = request.POST.get('l_commitdate')
        receiptdate = request.POST.get('l_receiptdate')
        shipinstruct = request.POST.get('l_shipinstruct')
        shipmode = request.POST.get('l_shipmode')
        comment = request.POST.get('l_comment')
        obj1 = models.Orders.objects.filter(l_orderkey=orderkey).first()
        sum = obj1.o_totalprice + extendedprice
        models.Orders.objects.filter(o_orderkey=orderkey).update(o_totalprice=sum)
        obj = models.Lineitem(l_orderkey=orderkey,l_partkey = partkey,l_suppkey =suppkey,
                                                            l_linenumber =linenumber,l_quantity=quantity,l_extendedprice=extendedprice,
                                                            l_discount=discount,l_tax=tax,l_returnflag=returnflag,l_linestatus=linestatus,
                                                            l_shipdate=shipdate,l_commitdate=commitdate,l_receiptdate=receiptdate,l_shipinstruct=shipinstruct,
                                                            l_shipmode=shipmode,l_comment=comment)
        obj.save()
        return HttpResponseRedirect("/DBHW/lineitemlist/")
    else:
        return render(request, 'lineitemadd.html')


def Order_list(request):
    order_list = models.Orders.objects.all()
    paginator = Paginator(order_list, 10)
    page = request.GET.get('page', 1)
    try:
        order = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        order = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        order = paginator.page(paginator.num_pages)
    return render(request, 'orderlist.html', {"order_list":order})
'''
@csrf_exempt
def Order_Edit(request,nid):
    if request.method == "POST":
        orderkey = request.POST.get('o_orderkey')
        custkey = request.POST.get('o_custkey')
        orderstatus = request.POST.get('o_orderstatus')
        totalprice = request.POST.get('o_totalprice')
        orderdate = request.POST.get('o_orderdate')
        orderpriority = request.POST.get('o_orderpriority')
        clerk = request.POST.get('o_clerk')
        shippriority = request.POST.get('o_shippriority')
        comment = request.POST.get('o_comment')
        models.Orders.objects.filter(o_orderkey=nid).update(o_orderkey=orderkey,o_custkey = custkey,o_orderstatus =orderstatus,
                                                            o_totalprice =totalprice,o_orderdate=orderdate,o_orderpriority=orderpriority,
                                                            o_clerk=clerk,o_shippriority=shippriority,o_comment=comment)
        return HttpResponseRedirect("/DBHW/orderlist/")
    else:
        obj = models.Orders.objects.filter(o_orderkey=nid).first()
        return render(request, 'orderlist.html', {"obj":obj})

'''
def Part_list(request):
    part_list = models.Part.objects.all()
    paginator = Paginator(part_list, 10)
    page = request.GET.get('page', 1)
    try:
        part = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        part = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        part = paginator.page(paginator.num_pages)
    return render(request, 'partlist.html', {"part_list":part})

@csrf_exempt
def Part_Edit(request,nid):
    if request.method == "POST":
        partkey = request.POST.get('p_partkey')
        name = request.POST.get('p_name')
        emfgr = request.POST.get('p_emfgr')
        brand = request.POST.get('p_brand')
        type = request.POST.get('p_type')
        size = request.POST.get('p_size')
        if size == '':
            size = 0
        container = request.POST.get('p_container')
        retailprice = request.POST.get('p_retailprice')
        if retailprice == '':
            retailprice = 0
        comment = request.POST.get('p_comment')
        models.Part.objects.filter(p_partkey=nid).update(p_partkey=partkey,p_name = name,p_emfgr=emfgr,
                                                            p_brand =brand,p_type=type,p_size=size,
                                                            p_container=container,p_retailprice=retailprice,p_comment=comment)
        return HttpResponseRedirect("/DBHW/partlist/")
    else:
        obj = models.Part.objects.filter(p_partkey=nid).first()
        return render(request, 'partedit.html', {"obj":obj})


def Part_delete(request, nid):
    models.Part.objects.filter(p_partkey=nid).delete()
    return render(request, 'partdelete.html')


@csrf_exempt
def Part_view(request, nid):
    obj = models.Part.objects.filter(p_partkey=nid).first()
    return render(request, 'partview.html', {"obj": obj})

@csrf_exempt
def Part_Add(request):
    if request.method == "POST":
        partkey = request.POST.get('p_partkey')
        name = request.POST.get('p_name')
        emfgr = request.POST.get('p_emfgr')
        brand = request.POST.get('p_brand')
        type = request.POST.get('p_type')
        size = request.POST.get('p_size')
        if size == '':
            size=0
        container = request.POST.get('p_container')
        retailprice = request.POST.get('p_retailprice')
        if retailprice == '':
            retailprice=0
        comment = request.POST.get('p_comment')
        obj = models.Part(p_partkey=partkey,p_name = name,p_emfgr=emfgr,
                         p_brand =brand,p_type=type,p_size=size,
                         p_container=container,p_retailprice=retailprice,p_comment=comment)
        obj.save()
        return HttpResponseRedirect("/DBHW/partlist/")
    else:
        return render(request, 'partadd.html')



def Partsupp_list(request):
    partsupp_list = models.Partsupp.objects.all()
    paginator = Paginator(partsupp_list, 10)
    page = request.GET.get('page', 1)
    try:
        partsupp = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        partsupp = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        partsupp = paginator.page(paginator.num_pages)
    return render(request, 'partsupplist.html', {"partsupp_list":partsupp})

@csrf_exempt
def Partsupp_Edit(request,nid):
    if request.method == "POST":
        partkey = request.POST.get('ps_partkey')
        suppkey = request.POST.get('ps_suppkey')
        availqty = request.POST.get('ps_availqty')
        supplycost = request.POST.get('ps_supplycost')
        comment = request.POST.get('ps_comment')

        models.Partsupp.objects.filter(ps_partkey=nid).update(ps_partkey=partkey, ps_suppkey =suppkey,ps_availqty=availqty,
                                                         ps_supplycost =supplycost,ps_comment=comment)
        return HttpResponseRedirect("/DBHW/partsupplist/")
    else:
        obj = models.Partsupp.objects.filter(ps_partkey=nid).first()
        return render(request, 'partsupplist.html', {"obj":obj})

def Partsupp_delete(request, nid):
    models.Partsupp.objects.filter(ps_partkey=nid).delete()
    return render(request, 'partsuppdelete.html')

@csrf_exempt
def Partsupp_Add(request):
    if request.method == "POST":
        partkey = request.POST.get('ps_partkey')
        suppkey = request.POST.get('ps_suppkey')
        availqty = request.POST.get('ps_availqty')
        supplycost = request.POST.get('ps_supplycost')
        comment = request.POST.get('ps_comment')

        obj = models.Partsupp(ps_partkey=partkey, ps_suppkey =suppkey,ps_availqty=availqty,
                                                         ps_supplycost =supplycost,ps_comment=comment)
        obj.save()
        return HttpResponseRedirect("/DBHW/partsupplist/")
    else:
        return render(request, 'partsuppadd.html')


@csrf_exempt
def Partsupp_view(request, nid):
    obj = models.Partsupp.objects.filter(ps_partkey=nid).first()
    return render(request, 'partsuppview.html', {"obj": obj})

def Region_list(request):
    region_list = models.Region.objects.all()
    paginator = Paginator(region_list, 10)
    page = request.GET.get('page', 1)
    try:
        region = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        region = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        region = paginator.page(paginator.num_pages)
    return render(request, 'regionlist.html', {"region_list":region})


@csrf_exempt
def Region_Edit(request,nid):
    if request.method == "POST":
        regionkey = request.POST.get('r_regionkey')
        name = request.POST.get('r_name')
        comment1 = request.POST.get('r_comment')
        supplycost = request.POST.get('ps_supplycost')
        comment2 = request.POST.get('ps_comment')
        models.Region.objects.filter(r_regionkey=nid).update(r_regionkey=regionkey,r_name = name,r_comment=comment1,
                                                         ps_supplycost =supplycost,ps_comment=comment2)
        return HttpResponseRedirect("/DBHW/regionlist/")
    else:
        obj = models.Region.objects.filter(r_regionkey=nid).first()
        return render(request, 'regionedit.html', {"obj":obj})

def Region_delete(request, nid):
    models.Region.objects.filter(r_regionkey=nid).delete()
    return render(request, 'regiondelete.html')


@csrf_exempt
def Region_view(request, nid):
    obj = models.Region.objects.filter(r_regionkey=nid).first()
    return render(request, 'regionview.html', {"obj": obj})

@csrf_exempt
def Region_Add(request):
    if request.method == "POST":
        regionkey = request.POST.get('r_regionkey')
        name = request.POST.get('r_name')
        comment1 = request.POST.get('r_comment')
        supplycost = request.POST.get('ps_supplycost')
        comment2 = request.POST.get('ps_comment')
        obj = models.Region(r_regionkey=regionkey,r_name = name,r_comment=comment1,
                                                         ps_supplycost =supplycost,ps_comment=comment2)
        obj.save()
        return HttpResponseRedirect("/DBHW/regionlist/")
    else:
        return render(request, 'regionadd.html')


def Supplier_list(request):
    supplier_list = models.Supplier.objects.all()
    paginator = Paginator(supplier_list, 10)
    page = request.GET.get('page', 1)
    try:
        supplier = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        supplier = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        supplier = paginator.page(paginator.num_pages)
    return render(request, 'supplierlist.html', {"supplier_list":supplier})

@csrf_exempt
def Supplier_Edit(request,nid):
    if request.method == "POST":
        suppkey = request.POST.get('s_suppkey')
        name = request.POST.get('s_name')
        address = request.POST.get('s_address')
        nationkey = request.POST.get('s_nationkey')
        phone = request.POST.get('s_phone')
        acctbal = request.POST.get('s_acctbal')
        comment = request.POST.get('s_comment')
        models.Supplier.objects.filter(s_suppkey=nid).update(s_suppkey=suppkey,s_name = name,s_address=address,
                                                           s_nationkey=nationkey,s_phone=phone,s_acctbal=acctbal,
                                                           s_comment=comment)
        return HttpResponseRedirect("/DBHW/supplierlist/")
    else:
        obj = models.Supplier.objects.filter(s_suppkey=nid).first()
        return render(request, 'supplieredit.html', {"obj":obj})

def Supplier_delete(request, nid):
    models.Supplier.objects.filter(s_suppkey=nid).delete()
    return render(request, 'supplierlist.html')


@csrf_exempt
def Supplier_view(request, nid):
    obj = models.Supplier.objects.filter(s_suppkey=nid).first()
    return render(request, 'supplierlist.html', {"obj": obj})

@csrf_exempt
def Supplier_Add(request):
    if request.method == "POST":
        suppkey = request.POST.get('s_suppkey')
        name = request.POST.get('s_name')
        address = request.POST.get('s_address')
        nationkey = request.POST.get('s_nationkey')
        phone = request.POST.get('s_phone')
        acctbal = request.POST.get('s_acctbal')
        comment = request.POST.get('s_comment')
        models.Supplier(s_suppkey=suppkey,s_name = name,s_address=address,
                                                           s_nationkey=nationkey,s_phone=phone,s_acctbal=acctbal,
                                                           s_comment=comment)
        return HttpResponseRedirect("/DBHW/supplierlist/")
    else:
        return render(request, 'supplieradd.html')