from django.urls import path,re_path,include
from DBHW.views import *
app_name = 'DBHW'
urlpatterns = [
    re_path(r'^customersearch/', Customer_search, name='customersearch'),
    re_path(r'^regionsearch/', Region_search, name='regionsearch'),
    re_path(r'^partsearch/', Part_search, name='partsearch'),
    re_path(r'^nationsearch/', Nation_search, name='nationsearch'),
    re_path(r'^suppliersearch/', Supplier_search, name='suppliersearch'),
    re_path(r'^nationlist/',Nation_list,name='nationlist'),
    re_path(r'^nationedit-(?P<nid>\d+)/',Nation_Edit,name='nationedit'),
    re_path(r'^nationadd/',Nation_add,name='nationadd'),
    re_path(r'^nationview-(?P<nid>\d+)/',Nation_view,name='nationview'),
    re_path(r'^nationdelete-(?P<nid>\d+)/',Nation_delete,name='nationdelete'),
    re_path(r'^customerlist/', Customer_list, name='customerlist'),
    re_path(r'^customeredit-(?P<nid>\d+)/', Customer_Edit, name='customeredit'),
    re_path(r'^customeradd/', Customer_add, name='customeradd'),
    re_path(r'^customerview-(?P<nid>\d+)/', Customer_view, name='customerview'),
    re_path(r'^customerdelete-(?P<nid>\d+)/', Customer_delete, name='customerdelete'),
    re_path(r'^lineitemlist/', Lineitem_list, name='lineitemlist'),
    re_path(r'^lineitemedit-(?P<nid>\d+)-(?P<uid>\d+)/',Lineitem_Edit, name='lineitemedit'),
    re_path(r'^lineitemadd/', Lineitem_Add, name='lineitemadd'),
    re_path(r'^lineitemview-(?P<nid>\d+)-(?P<uid>\d+)/', Lineitem_view, name='lineitemview'),
    re_path(r'^lineitemdelete-(?P<nid>\d+)-(?P<uid>\d+)/', Lineitem_delete, name='lineitemdelete'),
    re_path(r'^orderlist/', Order_list, name='orderlist'),
    re_path(r'^orderview-(?P<nid>\d+)/', Order_view, name='orderview'),
    re_path(r'^orderdelete-(?P<nid>\d+)/', Order_delete, name='orderdelete'),
    re_path(r'^orderadd/', Order_Add, name='orderadd'),
    re_path(r'^partlist/', Part_list, name='partlist'),
    re_path(r'^partedit-(?P<nid>\d+)/', Part_Edit, name='partedit'),
    re_path(r'^partadd/', Part_Add, name='partadd'),
    re_path(r'^partview-(?P<nid>\d+)/', Part_view, name='partview'),
    re_path(r'^partdelete-(?P<nid>\d+)/',Part_delete, name='partdelete'),
    re_path(r'^partsupplist/', Partsupp_list, name='partsupplist'),
    re_path(r'^partsuppedit-(?P<nid>\d+)-(?P<uid>\d+)/', Partsupp_Edit, name='partsuppedit'),
    re_path(r'^partsuppadd/', Partsupp_Add, name='partsuppadd'),
    re_path(r'^partsuppview-(?P<nid>\d+)-(?P<uid>\d+)/', Partsupp_view, name='partsuppview'),
    re_path(r'^partsuppdelete-(?P<nid>\d+)-(?P<uid>\d+)/',Partsupp_delete, name='partsuppdelete'),
    re_path(r'^regionlist/', Region_list, name='regionlist'),
    re_path(r'^regionedit-(?P<nid>\d+)/', Region_Edit, name='regionedit'),
    re_path(r'^regionadd/', Region_Add, name='regionadd'),
    re_path(r'^regionview-(?P<nid>\d+)/', Region_view, name='regionview'),
    re_path(r'^regiondelete-(?P<nid>\d+)/', Region_delete, name='regiondelete'),
    re_path(r'^supplierlist/', Supplier_list, name='supplierlist'),
    re_path(r'^supplieredit-(?P<nid>\d+)/', Supplier_Edit, name='supplieredit'),
    re_path(r'^supplieradd/', Supplier_Add, name='supplieradd'),
    re_path(r'^supplierview-(?P<nid>\d+)/', Supplier_view, name='supplierview'),
    re_path(r'^supplierdelete-(?P<nid>\d+)/', Supplier_delete, name='supplierdelete'),
 ]