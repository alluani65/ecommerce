from django.shortcuts import get_object_or_404, render
from.models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage



def allproductscat(request,cslug=None):
    cpage=None
    cproduct_list=None
    if cslug!=None:
        cpage=get_object_or_404(Category,slug=cslug)
        cproduct_list=Product.objects.all().filter(category=cpage,available=True)
    else:
        cproduct_list=Product.objects.all().filter(available=True)
    paginator=Paginator(cproduct_list,3)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        cproduct=paginator.page(page)
    except (InvalidPage,EmptyPage):
        cproduct=paginator.page(paginator.num_pages)

    return render(request,'category.html',{'category':cpage,'product':cproduct})

def productdetail(request,cslug,pslug):
    try:
        product=Product.objects.get(category__slug=cslug,slug=pslug)
    except Exception as e:
        raise e 
    return render(request,'products.html',{'products':product})