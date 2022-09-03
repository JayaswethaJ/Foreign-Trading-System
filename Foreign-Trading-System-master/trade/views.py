from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import CommodityForm, RequestForm
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Commodity ,Request, Trade
from django.db.models import F
# from django.utils import timezone
import datetime
# from datetime import date
# from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    UpdateView,
    ListView,
    DeleteView
)

# from django.db import transaction
# @transaction.non_atomic_requests
def my_view(request):
    # posts= Commodity.objects.exclude(exporterName = request.user)
    form = RequestForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.importerName = request.user
        obj.save()
        # for post in posts:
        #     print post
        #     print form.fields['commodityName']
        #     if post.commodityName == form.fields['commodityName']:
        #         # post.quantityAvailable = post.quantityAvailable - form.quantityAvailable
        #         return HttpResponseRedirect(reverse('mycommodities-view'))
        return HttpResponseRedirect(reverse('commodity-buy'))
    context = {
        'form' : form
    }
    return render(request,'trade/buy_commodity.html',context)

# @transaction.non_atomic_requests(using='other')
# def my_other_view(request):
#     do_stuff_on_the_other_database()

def request_page(request):
    if(request.GET.get('mybtn')):
        # print (request.GET.get('mytextbox'))
        mypythoncode.mypythonfunction( int(request.GET.get('mytextbox')) )

    return render(request,'trade/requests.html')

def commodityCreateView(request):
    form = CommodityForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.exporterName = request.user
        obj.save()
        return HttpResponseRedirect(reverse('mycommodities-view'))
    context = {
        'form' : form
    }
    return render(request,'trade/add_commodity.html',context)

def requestsShow(request):
    posts= Request.objects.filter(exporterName = request.user)
    # print (posts)
    context = {
        'posts' : posts
    }
    return render(request,'trade/requests.html',context)

def requestsSentShow(request):
    posts= Request.objects.filter(importerName = request.user)
    # print (posts)
    context = {
        'posts' : posts
    }
    return render(request,'trade/requestssent.html',context)

def homePageView(request):
    posts= Commodity.objects.exclude(exporterName = request.user)
    # print (posts)
    context = {
        'posts' : posts
    }
    return render(request,'trade/trader.html',context)


def logout_view(request):
    logout(request)
    return render(request, 'logged_out.html')

def myCommoditiesView(request):
    queryset = Commodity.objects.filter(exporterName = request.user)
    context = {
        'object_list' : queryset
    }
    return render(request, "trade/commodity_list.html", context)


def requestAccept(request,id):
    req = Request.objects.get(id=id)
    obj = Commodity.objects.get(commodityName=req.commodityName)
    # print req.quantityRequested
    # print obj.quantityAvailable
    if (req.quantityRequested > obj.quantityAvailable):
        return HttpResponse("Please request for less commodties")
    else:
        Commodity.objects.filter(commodityName = req.commodityName, exporterName = request.user).update(quantityAvailable=F('quantityAvailable') - req.quantityRequested)
        Trade.objects.create(commodityName=req.commodityName,importerName=req.importerName,exporterName=req.exporterName,datePerformed=datetime.datetime.now(),totalPrice=obj.price*req.quantityRequested)
        Request.objects.filter(id=id).delete()
        return redirect("requests-view")


def aboutView(request):
    return render(request, 'trade/about.html')
